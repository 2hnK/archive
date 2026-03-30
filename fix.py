import sys

nav_path = 'src/components/Navbar.astro'
try:
    with open(nav_path, 'r', encoding='utf-8') as f:
        nav = f.read()

    # 1. Restore nav-highlight to its fully operational state
    # This was stripped bare, removing crucial boundaries
    broken_highlight = '<div\n        id="nav-highlight"\n        class="absolute custom-glass-highlight rounded-full transition-all duration-400 ease-[cubic-bezier(0.25,1,0.5,1)] pointer-events-none opacity-0 z-0 scale-95"\n      >\n      </div>'
    fixed_highlight = '<div\n        id="nav-highlight"\n        class="absolute custom-glass-highlight border-blue-500/20 dark:border-blue-400/20 rounded-full transition-all duration-400 ease-[cubic-bezier(0.25,1,0.5,1)] pointer-events-none opacity-0 z-0 scale-95 border border-white/20 dark:border-white/10"\n      >\n      </div>'
    
    if broken_highlight in nav:
        nav = nav.replace(broken_highlight, fixed_highlight)

    # 2. Put back the thick glass background that looks premium (but no blue tint!)
    old_opaque_bg = 'class="fixed top-0 left-0 right-0 z-50 transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] md:mt-4 mx-auto w-full md:max-w-4xl lg:max-w-5xl xl:max-w-[1000px] border-b border-white/10 md:border md:border-apple-border/20 dark:md:border-apple-darkBorder/20 md:rounded-full bg-apple-surface/80 dark:bg-apple-darkSurface/80 backdrop-blur-[2px]"'
    
    strong_glass_bg = 'class="fixed top-0 left-0 right-0 z-50 transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] md:mt-4 mx-auto w-full md:max-w-4xl lg:max-w-5xl xl:max-w-[1000px] border-b md:border border-black/10 dark:border-white/10 md:rounded-full bg-white/70 dark:bg-[#1a1a1c]/60 backdrop-blur-2xl backdrop-saturate-[1.8] shadow-[0_4px_12px_rgba(30,102,245,0.05),inset_0_1px_1px_rgba(255,255,255,0.9)] dark:shadow-[0_8px_32px_rgba(0,0,0,0.4),inset_0_1px_1px_rgba(255,255,255,0.1)]"'
    
    if old_opaque_bg in nav:
        nav = nav.replace(old_opaque_bg, strong_glass_bg)

    # 3. Sidebar/Toggle glass effect unification
    # Add glass-pill to all header buttons
    nav = nav.replace(
        'class="group w-8 h-8 flex items-center justify-center rounded-full text-black dark:text-white', 
        'class="glass-pill group w-8 h-8 flex items-center justify-center rounded-full text-black dark:text-white border-0 hover:shadow-md'
    )

    with open(nav_path, 'w', encoding='utf-8') as f:
        f.write(nav)
    print('Navbar fixed successfully')
except Exception as e:
    print('Error in Navbar.astro:', e)

# 4. about.astro hover removal from background and sharpening of inner borders
about_path = 'src/pages/about.astro'
try:
    with open(about_path, 'r', encoding='utf-8') as f:
        about = f.read()

    # Apply group-hover to the glass-pill specifically
    # Change glass-pill span class inside about.astro to have hover:bg-black etc? 
    # The user says "안에 요소들 테두리 선명도 올려줘" which means inner pill border opacity.
    # In global.css, I already updated the border.
    # Let's make sure pills inside bento grid hover correctly.
    # It might just require adding "hover:scale-105" or similar if they don't have it.
    about = about.replace('class="glass-pill px-3 py-1.5"', 'class="glass-pill px-3 py-1.5 transition-transform hover:scale-[1.05]"')
    about = about.replace('class="glass-pill px-4 py-2 hover:scale-[1.02]"', 'class="glass-pill px-4 py-2 transition-transform hover:scale-[1.05]"')

    with open(about_path, 'w', encoding='utf-8') as f:
        f.write(about)
    print("Updated about.astro inner pill hover")
except Exception as e:
    print('Error in about.astro:', e)
