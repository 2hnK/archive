import io

BENTO_BOX_HTML = """      <!-- Capabilities & Milestones (Bento Box) -->
      <section class="max-w-[900px] mx-auto px-6 mb-32">
        <div class="mb-10 reveal-up">
          <span class="text-[0.75rem] tracking-[0.08em] font-medium uppercase text-apple-textMuted dark:text-apple-darkTextMuted mb-2 block">Capabilities</span>
          <h2 class="text-3xl font-bold tracking-tight text-apple-text dark:text-apple-darkText">역량 및 자격</h2>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 auto-rows-[minmax(180px,auto)]">
          
          <!-- Backend Foundation (Span 2) -->
          <div class="md:col-span-2 bg-apple-surface dark:bg-[#1a1a1a] p-8 rounded-[2rem] border border-apple-border/50 dark:border-apple-darkBorder reveal-up transition-shadow hover:shadow-lg dark:hover:shadow-white/5 flex flex-col justify-between group">
            <div class="mb-6">
              <span class="text-apple-textMuted dark:text-apple-darkTextMuted text-xs font-semibold tracking-wider uppercase mb-1 block">Core</span>
              <h3 class="text-2xl font-bold text-apple-text dark:text-apple-darkText">Backend Foundation</h3>
            </div>
            <div class="flex flex-wrap gap-4">
              <!-- Java -->
              <div class="flex items-center gap-3 bg-white/50 dark:bg-white/5 px-4 py-3 rounded-2xl border border-black/5 dark:border-white/5 backdrop-blur-md transition-transform hover:scale-[1.02]">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg" alt="Java" class="w-8 h-8 object-contain" />
                <span class="font-semibold text-sm text-apple-text dark:text-apple-darkText">Java</span>
              </div>
              <!-- Python -->
              <div class="flex items-center gap-3 bg-white/50 dark:bg-white/5 px-4 py-3 rounded-2xl border border-black/5 dark:border-white/5 backdrop-blur-md transition-transform hover:scale-[1.02]">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" alt="Python" class="w-8 h-8 object-contain" />
                <span class="font-semibold text-sm text-apple-text dark:text-apple-darkText">Python</span>
              </div>
              <!-- Spring -->
              <div class="flex items-center gap-3 bg-white/50 dark:bg-white/5 px-4 py-3 rounded-2xl border border-black/5 dark:border-white/5 backdrop-blur-md transition-transform hover:scale-[1.02]">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/spring/spring-original.svg" alt="Spring" class="w-8 h-8 object-contain" />
                <span class="font-semibold text-sm text-apple-text dark:text-apple-darkText">Spring</span>
              </div>
            </div>
          </div>

          <!-- Acquisitions / Certifications (Span 1, Row Span 2) -->
          <div class="md:col-span-1 md:row-span-2 bg-gradient-to-br from-[#f5f5f7] to-[#e8e8ed] dark:from-[#1a1a1a] dark:to-[#111111] p-8 rounded-[2rem] border border-apple-border/50 dark:border-apple-darkBorder reveal-up stagger-1 transition-shadow hover:shadow-lg dark:hover:shadow-white/5 flex flex-col group relative overflow-hidden">
            <div class="absolute -right-10 -top-10 w-40 h-40 bg-blue-500/10 dark:bg-blue-500/20 rounded-full blur-3xl group-hover:bg-blue-500/20 transition-colors"></div>
            <div class="mb-8 relative z-10">
              <span class="text-apple-textMuted dark:text-apple-darkTextMuted text-xs font-semibold tracking-wider uppercase mb-1 block">Milestones</span>
              <h3 class="text-2xl font-bold text-apple-text dark:text-apple-darkText">Acquisitions</h3>
            </div>
            <div class="space-y-4 relative z-10 flex-1 flex flex-col justify-center">
              <!-- 정보처리기사 -->
              <div class="flex items-center gap-4 bg-white/80 dark:bg-white/5 p-4 rounded-2xl border border-black/5 dark:border-white/5 backdrop-blur-md transition-transform hover:scale-[1.02]">
                <div class="w-10 h-10 rounded-xl bg-blue-50 dark:bg-blue-500/20 flex flex-shrink-0 items-center justify-center text-blue-600 dark:text-blue-400">
                  <span class="material-symbols-outlined text-xl">workspace_premium</span>
                </div>
                <div>
                  <h4 class="font-bold text-sm text-apple-text dark:text-apple-darkText">정보처리기사</h4>
                  <span class="text-[0.7rem] font-medium text-apple-textMuted dark:text-apple-darkTextMuted">2025.09.12 취득</span>
                </div>
              </div>
              <!-- SQLD -->
              <div class="flex items-center gap-4 bg-white/80 dark:bg-white/5 p-4 rounded-2xl border border-black/5 dark:border-white/5 backdrop-blur-md transition-transform hover:scale-[1.02]">
                <div class="w-10 h-10 rounded-xl bg-emerald-50 dark:bg-emerald-500/20 flex flex-shrink-0 items-center justify-center text-emerald-600 dark:text-emerald-400">
                  <span class="material-symbols-outlined text-xl">database</span>
                </div>
                <div>
                  <h4 class="font-bold text-sm text-apple-text dark:text-apple-darkText">SQLD</h4>
                  <span class="text-[0.7rem] font-medium text-apple-textMuted dark:text-apple-darkTextMuted">2025.06.27 취득</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Data Stores (Span 1) -->
          <div class="md:col-span-1 bg-apple-surface dark:bg-[#1a1a1a] p-8 rounded-[2rem] border border-apple-border/50 dark:border-apple-darkBorder reveal-up stagger-2 transition-shadow hover:shadow-lg dark:hover:shadow-white/5 flex flex-col justify-between group">
            <div class="mb-6">
              <span class="text-apple-textMuted dark:text-apple-darkTextMuted text-xs font-semibold tracking-wider uppercase mb-1 block">Storage</span>
              <h3 class="text-xl font-bold text-apple-text dark:text-apple-darkText">Data Stores</h3>
            </div>
            <div class="grid grid-cols-3 gap-3">
              <!-- MySQL -->
              <div class="bg-white/50 dark:bg-white/5 aspect-square rounded-2xl flex items-center justify-center border border-black/5 dark:border-white/5 transition-transform hover:scale-[1.05]" title="MySQL">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg" alt="MySQL" class="w-8 h-8 object-contain" />
              </div>
              <!-- PostgreSQL -->
              <div class="bg-white/50 dark:bg-white/5 aspect-square rounded-2xl flex items-center justify-center border border-black/5 dark:border-white/5 transition-transform hover:scale-[1.05]" title="PostgreSQL">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" alt="PostgreSQL" class="w-8 h-8 object-contain" />
              </div>
              <!-- Redis -->
              <div class="bg-white/50 dark:bg-white/5 aspect-square rounded-2xl flex items-center justify-center border border-black/5 dark:border-white/5 transition-transform hover:scale-[1.05]" title="Redis">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/redis/redis-original.svg" alt="Redis" class="w-8 h-8 object-contain" />
              </div>
            </div>
          </div>

          <!-- Infrastructure (Span 1) -->
          <div class="md:col-span-1 bg-apple-surface dark:bg-[#1a1a1a] p-8 rounded-[2rem] border border-apple-border/50 dark:border-apple-darkBorder reveal-up stagger-3 transition-shadow hover:shadow-lg dark:hover:shadow-white/5 flex flex-col justify-between group">
            <div class="mb-6">
              <span class="text-apple-textMuted dark:text-apple-darkTextMuted text-xs font-semibold tracking-wider uppercase mb-1 block">Cloud & DevOps</span>
              <h3 class="text-xl font-bold text-apple-text dark:text-apple-darkText">Infrastructure</h3>
            </div>
            <div class="flex gap-4">
              <!-- Docker -->
              <div class="flex-1 bg-white/50 dark:bg-white/5 py-4 rounded-2xl flex flex-col items-center justify-center gap-2 border border-black/5 dark:border-white/5 transition-transform hover:scale-[1.05]">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" alt="Docker" class="w-8 h-8 object-contain" />
                <span class="text-[0.7rem] font-bold text-apple-text dark:text-apple-darkText">Docker</span>
              </div>
              <!-- AWS -->
              <div class="flex-1 bg-white/50 dark:bg-white/5 py-4 rounded-2xl flex flex-col items-center justify-center gap-2 border border-black/5 dark:border-white/5 transition-transform hover:scale-[1.05]">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="AWS" class="w-8 h-8 object-contain" />
              </div>
            </div>
          </div>
          
        </div>
      </section>
"""

file_path = r"d:\archive\src\pages\about.astro"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# find exact ranges
# find "<!-- Tech Stack Grid" to "</section>" inside that section
def find_section(lines, start_marker, end_marker):
    start = -1
    for i, line in enumerate(lines):
        if start_marker in line:
            start = i
            break
    if start == -1: return -1, -1
    end = -1
    for i in range(start, len(lines)):
        if end_marker in line and "</section>" in lines[i]:
            end = i
            break
    return start, end

# Let's just use exact line numbers since we know them:
# 50 to 123 for Tech Stack (inclusive = 49 to 123 Python 0-idx)
# 125 to 169 for Timeline (inclusive = 124 to 168)
# 171 to 200 for Certifications

new_lines = []
new_lines.extend(lines[:49])
new_lines.append(BENTO_BOX_HTML)
new_lines.extend(lines[124:169])
new_lines.extend(lines[200:])

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("done")
