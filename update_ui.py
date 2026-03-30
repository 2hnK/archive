import sys

# 1. Update global.css hover effects
try:
    with open('src/styles/global.css', 'r', encoding='utf-8') as f:
        css = f.read()

    hover_css = '''  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.glass-panel:hover {
  transform: translateY(-4px) scale(1.01);
  box-shadow: 
    0 12px 30px rgba(0, 0, 0, 0.08),
    0 24px 60px rgba(0, 0, 0, 0.04),
    inset 0 1px 1px rgba(255, 255, 255, 0.9);
}

.dark .glass-panel {'''

    css = css.replace('''  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.dark .glass-panel {''', hover_css)

    dark_hover_css = '''  inset 0 1px 1px rgba(255, 255, 255, 0.06);
}

.dark .glass-panel:hover {
  box-shadow: 
    0 12px 30px rgba(0, 0, 0, 0.3),
    0 24px 60px rgba(0, 0, 0, 0.2),
    inset 0 1px 2px rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.glass-pill {'''

    css = css.replace('''  inset 0 1px 1px rgba(255, 255, 255, 0.06);
}

.glass-pill {''', dark_hover_css)

    with open('src/styles/global.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated global.css")
except Exception as e:
    print(f"Error in global.css: {e}")


# 2. Add glass-pill to Explore Topics
for filepath in ['src/pages/index.astro', 'src/pages/articles/index.astro']:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        target = 'px-3 py-1.5 rounded-[10px] border border-black/10 dark:border-white/10 text-[11px] font-bold tracking-widest text-apple-text dark:text-apple-darkText hover:text-[#1e66f5] dark:hover:text-[#89b4fa] hover:border-[#1e66f5]/30 dark:hover:border-[#89b4fa]/30 transition-colors uppercase bg-black/[0.02] dark:bg-white/[0.02] hover:bg-black/[0.05] dark:hover:bg-white/[0.05] backdrop-blur-md'
        replacement = 'glass-pill px-4 py-1.5 text-[11px] font-bold tracking-widest text-apple-text dark:text-apple-darkText hover:text-white dark:hover:text-black hover:bg-black dark:hover:bg-white transition-all duration-300 transform hover:scale-[1.05] uppercase border-black/5 dark:border-white/10 shadow-sm'
        
        content = content.replace(target, replacement)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated Explore Topics in {filepath}")
    except Exception as e:
        print(f'Error processing {filepath}: {e}')


# 3. TimeProgress thickness and font
try:
    with open('src/components/TimeProgress.astro', 'r', encoding='utf-8') as f:
        tp = f.read()

    # Font adjustments
    tp = tp.replace(
        '${mini ? "text-[11px]" : "text-[14px]"} font-medium',
        '${mini ? "text-[11px]" : "text-[14px]"} font-semibold tracking-wide font-sans'
    )
    tp = tp.replace(
        'class=\"${mini ? "text-[9px]" : "text-[12px]"} text-gray-400 font-medium\"',
        'class=\"${mini ? "text-[9px]" : "text-[12px]"} text-[#6c6f85] dark:text-[#a6adc8] font-bold tracking-wider\"'
    )

    # Thickness adjustments
    tp = tp.replace('${mini ? "h-[6px]" : "h-2.5"}', 'h-[6px]')

    with open('src/components/TimeProgress.astro', 'w', encoding='utf-8') as f:
        f.write(tp)
    print("Updated TimeProgress.astro")
except Exception as e:
    print(f"Error in TimeProgress.astro: {e}")


# 4. Enhance Navbar Glassmorphism
try:
    with open('src/components/Navbar.astro', 'r', encoding='utf-8') as f:
        nav = f.read()

    nav_target = 'border-b border-white/10 md:border md:border-apple-border/20 dark:md:border-apple-darkBorder/20 md:rounded-full bg-apple-surface/80 dark:bg-apple-darkSurface/80 backdrop-blur-[2px]'
    nav_replacement = 'border-b md:border border-black/10 dark:border-white/10 md:rounded-full bg-white/60 dark:bg-[#1a1a1c]/60 backdrop-blur-2xl backdrop-saturate-[1.5] shadow-[0_2px_10px_rgba(0,0,0,0.05),inset_0_1px_1px_rgba(255,255,255,0.8)] dark:shadow-[0_4px_16px_rgba(0,0,0,0.3),inset_0_1px_1px_rgba(255,255,255,0.06)]'

    nav = nav.replace(nav_target, nav_replacement)
    with open('src/components/Navbar.astro', 'w', encoding='utf-8') as f:
        f.write(nav)
    print("Updated Navbar.astro border effect")
except Exception as e:
    print(f"Error in Navbar.astro: {e}")
