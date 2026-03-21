/**
 * Custom Liquid Glass Highlight Filter
 * Ported from user's Shader (dynamic-frame-layout)
 * Generates an SDF-based displacement map on a canvas, converts to feImage,
 * and sets up a global SVG filter for `.custom-glass-highlight` elements to use.
 */
(function() {
  'use strict';

  function smoothStep(a, b, t) {
    t = Math.max(0, Math.min(1, (t - a) / (b - a)));
    return t * t * (3 - 2 * t);
  }

  function length(x, y) {
    return Math.sqrt(x * x + y * y);
  }

  function roundedRectSDF(x, y, width, height, radius) {
    const qx = Math.abs(x) - width + radius;
    const qy = Math.abs(y) - height + radius;
    return Math.min(Math.max(qx, qy), 0) + length(Math.max(qx, 0), Math.max(qy, 0)) - radius;
  }

  function createDisplacementMapBase64() {
    const size = 256;
    const canvas = document.createElement('canvas');
    canvas.width = size;
    canvas.height = size;
    const ctx = canvas.getContext('2d');
    const imgData = ctx.createImageData(size, size);
    const data = imgData.data;

    let maxScale = 0;
    const rawValues = [];

    // The logic from user's fragment code:
    for (let i = 0; i < data.length; i += 4) {
      const idx = i / 4;
      const x = idx % size;
      const y = Math.floor(idx / size);
      const uvX = x / size;
      const uvY = y / size;

      const ix = uvX - 0.5;
      const iy = uvY - 0.5;

      // roundedRectSDF params from user script
      const distanceToEdge = roundedRectSDF(ix, iy, 0.3, 0.2, 0.6);
      const displacement = smoothStep(0.8, 0, distanceToEdge - 0.15);
      const scaled = smoothStep(0, 1, displacement);

      // pos.x and pos.y after texture sampling equivalent
      const posX = ix * scaled + 0.5;
      const posY = iy * scaled + 0.5;

      const dx = posX * size - x;
      const dy = posY * size - y;

      maxScale = Math.max(maxScale, Math.abs(dx), Math.abs(dy));
      rawValues.push(dx, dy);
    }

    maxScale *= 0.5;
    if (maxScale === 0) maxScale = 1;

    let valIdx = 0;
    for (let i = 0; i < data.length; i += 4) {
      const r = rawValues[valIdx++] / maxScale + 0.5;
      const g = rawValues[valIdx++] / maxScale + 0.5;
      data[i] = r * 255;
      data[i + 1] = g * 255;
      data[i + 2] = 0;
      data[i + 3] = 255; // Alpha
    }

    ctx.putImageData(imgData, 0, 0);
    return canvas.toDataURL('image/png');
  }

  function injectFilter() {
    if (document.getElementById('custom-liquid-glass-svg')) return;

    const b64 = createDisplacementMapBase64();

    const svgNs = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(svgNs, 'svg');
    svg.setAttribute('id', 'custom-liquid-glass-svg');
    svg.style.cssText = 'position: absolute; width: 0; height: 0; pointer-events: none;';

    // Using objectBoundingBox allows the map to stretch to the element's actual dimensions
    svg.innerHTML = `
      <defs>
        <filter id="liquid-glass-highlight-filter" filterUnits="objectBoundingBox" primitiveUnits="objectBoundingBox" x="0" y="0" width="1" height="1" color-interpolation-filters="sRGB">
          <feImage href="${b64}" width="1" height="1" preserveAspectRatio="none" result="map" />
          <feDisplacementMap in="SourceGraphic" in2="map" scale="0.1" xChannelSelector="R" yChannelSelector="G" result="displaced" />
          <feMerge>
            <feMergeNode in="displaced" />
          </feMerge>
        </filter>
      </defs>
    `;

    document.body.appendChild(svg);
  }

  // Load in Astro
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectFilter);
  } else {
    injectFilter();
  }
  document.addEventListener('astro:page-load', injectFilter);

})();
