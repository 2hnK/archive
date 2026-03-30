import sys

with open("src/pages/about.astro", "r", encoding="utf-8") as f:
    text = f.read()

start_marker = "          <!-- Language (Span 1) -->"
end_marker = "        </div>\n      </section>"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker, start_idx) + len(end_marker)

if start_idx == -1 or end_idx == -1 + len(end_marker):
    print("Markers not found!")
    sys.exit(1)

new_content = """          <!-- Core Stack (Span 1) -->
          <div class="sm:col-span-1 bg-white/50 dark:bg-apple-darkSurface p-6 rounded-[1.5rem] border border-black/5 dark:border-white/5 shadow-sm reveal-up flex flex-col justify-between">
            <div class="mb-4">
              <span class="text-apple-textMuted dark:text-apple-darkTextMuted text-[10px] font-bold tracking-wider uppercase mb-1 block">Foundations</span>
              <h3 class="text-[17px] font-bold text-apple-text dark:text-apple-darkText">Core Stack</h3>
            </div>
            <div class="flex flex-wrap gap-2.5">
              <!-- Java -->
              <div class="flex items-center gap-2 bg-white/50 dark:bg-white/5 px-3 py-2 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:scale-[1.05] hover:bg-white dark:hover:bg-white/20 shadow-sm cursor-default">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg" alt="Java" class="w-5 h-5 object-contain" />
                <span class="font-semibold text-[13px] text-apple-text dark:text-apple-darkText">Java</span>
              </div>
              <!-- Python -->
              <div class="flex items-center gap-2 bg-white/50 dark:bg-white/5 px-3 py-2 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:scale-[1.05] hover:bg-white dark:hover:bg-white/20 shadow-sm cursor-default">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" alt="Python" class="w-5 h-5 object-contain" />
                <span class="font-semibold text-[13px] text-apple-text dark:text-apple-darkText">Python</span>
              </div>
              <!-- Spring -->
              <div class="flex items-center gap-2 bg-white/50 dark:bg-white/5 px-3 py-2 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:scale-[1.05] hover:bg-white dark:hover:bg-white/20 shadow-sm cursor-default">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/spring/spring-original.svg" alt="Spring" class="w-5 h-5 object-contain" />
                <span class="font-semibold text-[13px] text-apple-text dark:text-apple-darkText">Spring</span>
              </div>
            </div>
          </div>

          <!-- AI Ecosystem (Span 1) -->
          <div class="sm:col-span-1 bg-white/50 dark:bg-apple-darkSurface p-6 rounded-[1.5rem] border border-black/5 dark:border-white/5 shadow-sm reveal-up stagger-1 flex flex-col justify-between">
            <div class="mb-4">
              <span class="text-apple-textMuted dark:text-apple-darkTextMuted text-[10px] font-bold tracking-wider uppercase mb-1 block">Learning</span>
              <h3 class="text-[17px] font-bold text-apple-text dark:text-apple-darkText">AI Ecosystem</h3>
            </div>
            <div class="flex flex-wrap gap-2.5">
              <!-- Spring AI -->
              <div class="flex items-center gap-1.5 bg-black/5 dark:bg-white/5 px-3 py-2 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:scale-[1.05] shadow-sm cursor-default opacity-60">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/spring/spring-original.svg" alt="Spring AI" class="w-[14px] h-[14px] object-contain" />
                <span class="font-semibold text-[12px] text-apple-text dark:text-apple-darkText">Spring AI</span>
              </div>
              <!-- LangChain -->
              <div class="flex items-center gap-1.5 bg-black/5 dark:bg-white/5 px-3 py-2 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:scale-[1.05] shadow-sm cursor-default opacity-60">
                <svg fill="currentColor" role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="w-[14px] h-[14px]">
                  <title>LangChain</title>
                  <path d="M6.0988 5.9175C2.7359 5.9175 0 8.6462 0 12s2.736 6.0825 6.0988 6.0825h11.8024C21.2641 18.0825 24 15.3538 24 12s-2.736-6.0825-6.0988-6.0825ZM5.9774 7.851c.493.0124 1.02.2496 1.273.6228.3673.4592.4778 1.0668.8944 1.4932.5604.6118 1.199 1.1505 1.7161 1.802.4892.5954.8386 1.2937 1.1436 1.9975.1244.2335.1257.5202.31.7197.0908.1204.5346.4483.4383.5645.0555.1204.4702.286.3263.4027-.1944.04-.4129.0476-.5616-.1074-.0549.126-.183.0596-.2819.0432a4 4 0 0 0-.025.0736c-.3288.0219-.5754-.3126-.732-.565-.3111-.168-.6642-.2702-.982-.446-.0182.2895.0452.6485-.231.8353-.014.5565.8436.0656.9222.4804-.061.0067-.1286-.0095-.1774.0373-.2239.2172-.4805-.1645-.7385-.007-.3464.174-.3808.3161-.8096.352-.0237-.0359-.0143-.0592.0059-.0811.1207-.1399.1295-.3046.3356-.3643-.2122-.0334-.3899.0833-.5686.1757-.2323.095-.2304-.2141-.5878.0164-.0396-.0322-.0208-.0615.0018-.0864.0908-.1107.2102-.127.345-.1208-.663-.3686-.9751.4507-1.2813.0432-.092.0243-.1265.1068-.1845.1652-.05-.0548-.0123-.1212-.0099-.1857-.0598-.028-.1356-.041-.1179-.1366-.1171-.0395-.1988.0295-.286.0952-.0787-.0608.0532-.1492.0776-.2125.0702-.1216.23-.025.3111-.1126.2306-.1308.552.0814.8155.0455.203.0255.4544-.1825.3526-.39-.2171-.2767-.179-.6386-.1839-.9695-.0268-.1929-.491-.4382-.6252-.6462-.1659-.1873-.295-.4047-.4243-.6182-.4666-.9008-.3198-2.0584-.9077-2.8947-.266.1466-.6125.0774-.8418-.119-.1238.1125-.1292.2598-.139.4161-.297-.2962-.2593-.8559-.022-1.1855.0969-.1302.2127-.2373.342-.3316.0292-.0213.0391-.0419.0385-.0747.1174-.5267.5764-.7391 1.0694-.7267m12.4071.46c.5575 0 1.0806.2159 1.474.6082s.61.9145.61 1.4704c0 .556-.2167 1.078-.61 1.4698v.0006l-.902.8995a2.08 2.08 0 0 1-.8597.5166l-.0164.0047-.0058.0164a2.05 2.05 0 0 1-.474.7308l-.9018.8995c-.3934.3924-.917.6083-1.4745.6083s-1.0806-.216-1.474-.6083c-.813-.8107-.813-2.1294 0-2.9402l.9019-.8995a2.056 2.056 0 0 1 .858-.5143l.017-.0053.0058-.0158a2.07 2.07 0 0 1 .4752-.7337l.9018-.8995c.3934-.3924.9171-.6083 1.4745-.6083zm0 .8965a1.18 1.18 0 0 0-.8388.3462l-.9018.8995a1.181 1.181 0 0 0-.3427.9252l.0053.0572c.0323.2652.149.5044.3374.6917.13.1296.2733.2114.4471.2686a.9.9 0 0 1 .014.1582.884.884 0 0 1-.2609.6304l-.0554.0554c-.3013-.1028-.5525-.253-.7794-.4792a2.06 2.06 0 0 1-.5761-1.0968l-.0099-.0578-.0461.0368a1.1 1.1 0 0 0-.0876.0794l-.9024.8995c-.4623.461-.4623 1.212 0 1.673.2311.2305.535.346.8394.3461.3043 0 .6077-.1156.8388-.3462l.9019-.8995c.4623-.461.4623-1.2113 0-1.673a1.17 1.17 0 0 0-.4367-.2749 1 1 0 0 1-.014-.1611c0-.2591.1023-.505.2901-.6923.3019.1028.57.2694.7962.495.3007.2999.4994.679.5756 1.0968l.0105.0578.0455-.0373a1.1 1.1 0 0 0 .0887-.0794l.902-.8996c.4622-.461.4628-1.2124 0-1.6735a1.18 1.18 0 0 0-.8395-.3462Zm-9.973 5.1567-.0006.0006c-.0793.3078-.1048.8318-.506.847-.033.1776.1228.2445.2655.1874.141-.0645.2081.0508.2557.1657.2177.0317.5394-.0725.5516-.3298-.325-.1867-.4253-.5418-.5662-.8709" />
                </svg>
                <span class="font-semibold text-[12px] text-apple-text dark:text-apple-darkText">LangChain</span>
              </div>
            </div>
          </div>

          <!-- Data Stores (Span 1) -->
          <div class="sm:col-span-1 bg-white/50 dark:bg-apple-darkSurface p-6 rounded-[1.5rem] border border-black/5 dark:border-white/5 shadow-sm reveal-up stagger-2 flex flex-col justify-between">
            <div class="mb-4">
              <span class="text-apple-textMuted dark:text-apple-darkTextMuted text-[10px] font-bold tracking-wider uppercase mb-1 block">Storage</span>
              <h3 class="text-[17px] font-bold text-apple-text dark:text-apple-darkText">Data Stores</h3>
            </div>
            <div class="flex flex-wrap gap-2.5">
              <!-- MySQL -->
              <div class="flex items-center gap-2 bg-white/50 dark:bg-white/5 px-3 py-2 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:scale-[1.05] hover:bg-white dark:hover:bg-white/20 shadow-sm cursor-default">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg" alt="MySQL" class="w-5 h-5 object-contain" />
                <span class="font-semibold text-[13px] text-apple-text dark:text-apple-darkText">MySQL</span>
              </div>
              <!-- PostgreSQL -->
              <div class="flex items-center gap-2 bg-white/50 dark:bg-white/5 px-3 py-2 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:scale-[1.05] hover:bg-white dark:hover:bg-white/20 shadow-sm cursor-default">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" alt="PostgreSQL" class="w-5 h-5 object-contain" />
                <span class="font-semibold text-[13px] text-apple-text dark:text-apple-darkText">PostgreSQL</span>
              </div>
              <!-- Redis -->
              <div class="flex items-center gap-2 bg-white/50 dark:bg-white/5 px-3 py-2 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:scale-[1.05] hover:bg-white dark:hover:bg-white/20 shadow-sm cursor-default">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/redis/redis-original.svg" alt="Redis" class="w-5 h-5 object-contain" />
                <span class="font-semibold text-[13px] text-apple-text dark:text-apple-darkText">Redis</span>
              </div>
            </div>
          </div>

          <!-- Infrastructure (Span 1) -->
          <div class="sm:col-span-1 bg-white/50 dark:bg-apple-darkSurface p-6 rounded-[1.5rem] border border-black/5 dark:border-white/5 shadow-sm reveal-up stagger-3 flex flex-col justify-between">
            <div class="mb-4">
              <span class="text-apple-textMuted dark:text-apple-darkTextMuted text-[10px] font-bold tracking-wider uppercase mb-1 block">Cloud & DevOps</span>
              <h3 class="text-[17px] font-bold text-apple-text dark:text-apple-darkText">Infrastructure</h3>
            </div>
            <div class="flex flex-wrap gap-2.5">
              <!-- Docker -->
              <div class="flex items-center gap-2 bg-white/50 dark:bg-white/5 px-3 py-2 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:scale-[1.05] hover:bg-white dark:hover:bg-white/20 shadow-sm cursor-default">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" alt="Docker" class="w-5 h-5 object-contain" />
                <span class="font-semibold text-[13px] text-apple-text dark:text-apple-darkText">Docker</span>
              </div>
              <!-- AWS -->
              <div class="flex items-center gap-2 bg-white/50 dark:bg-white/5 px-3 py-2 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:scale-[1.05] hover:bg-white dark:hover:bg-white/20 shadow-sm cursor-default">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="AWS" class="w-7 h-7 object-contain" />
                <span class="font-semibold text-[13px] text-apple-text dark:text-apple-darkText">AWS</span>
              </div>
            </div>
          </div>

          <!-- Acquisitions / Certifications (Span 2) -->
          <div class="sm:col-span-2 bg-white/50 dark:bg-apple-darkSurface px-6 py-5 rounded-[1.5rem] border border-black/5 dark:border-white/5 shadow-sm reveal-up flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
            <div class="flex-shrink-0">
              <span class="text-apple-textMuted dark:text-apple-darkTextMuted text-[10px] font-bold tracking-wider uppercase mb-1 block">Milestones</span>
              <h3 class="text-[17px] font-bold text-apple-text dark:text-apple-darkText leading-none">Certifications</h3>
            </div>
            <div class="flex flex-col sm:flex-row gap-4 items-center sm:items-end justify-start sm:justify-end w-full">
              <!-- 정보처리기사 -->
              <div class="flex items-center gap-2.5 bg-white/60 dark:bg-white/5 px-4 py-2.5 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_8px_20px_rgba(59,130,246,0.15)] dark:hover:shadow-[0_8px_20px_rgba(59,130,246,0.25)] ring-1 ring-transparent hover:ring-blue-500/20 cursor-default group">
                <div class="w-[30px] h-[30px] rounded-full bg-white dark:bg-apple-darkSurface flex flex-shrink-0 items-center justify-center border border-black/5 dark:border-white/10 overflow-hidden shadow-sm p-[3px] group-hover:shadow-[0_0_12px_rgba(59,130,246,0.5)] transition-shadow duration-300">
                  <Image src={engineerLogo} alt="정보처리기사 로고" class="w-full h-full object-contain rounded-full transition-transform duration-300 group-hover:scale-110" />
                </div>
                <div class="flex flex-col justify-center leading-tight pt-0.5">
                  <h4 class="font-bold text-[13px] text-apple-text dark:text-apple-darkText group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">정보처리기사</h4>
                  <span class="text-[9px] font-medium text-apple-textMuted dark:text-apple-darkTextMuted">2025.09.12</span>
                </div>
              </div>
              <!-- SQLD -->
              <div class="flex items-center gap-2.5 bg-white/60 dark:bg-white/5 px-4 py-2.5 rounded-full border border-black/5 dark:border-white/5 backdrop-blur-md transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_8px_20px_rgba(16,185,129,0.15)] dark:hover:shadow-[0_8px_20px_rgba(16,185,129,0.25)] ring-1 ring-transparent hover:ring-emerald-500/20 cursor-default group">
                <div class="w-[30px] h-[30px] rounded-full bg-white dark:bg-apple-darkSurface flex flex-shrink-0 items-center justify-center border border-black/5 dark:border-white/10 overflow-hidden shadow-sm p-[3px] group-hover:shadow-[0_0_12px_rgba(16,185,129,0.5)] transition-shadow duration-300">
                  <Image src={sqldLogo} alt="SQLD 로고" class="w-full h-full object-contain rounded-full transition-transform duration-300 group-hover:scale-110" />
                </div>
                <div class="flex flex-col justify-center leading-tight pt-0.5">
                  <h4 class="font-bold text-[13px] text-apple-text dark:text-apple-darkText group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors">SQLD</h4>
                  <span class="text-[9px] font-medium text-apple-textMuted dark:text-apple-darkTextMuted">2025.06.27</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>"""

final_text = text[:start_idx] + new_content + text[end_idx:]

with open("src/pages/about.astro", "w", encoding="utf-8") as f:
    f.write(final_text)

print("Replacement successful.")
