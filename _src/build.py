"""Builds the static pages of guitin.co.kr from the parts below.
Run:  python3 _src/build.py   (writes *.html in the site root)
Edit copy here, then rebuild. The _src folder is not deployed (.vercelignore)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://guitin.co.kr'
KAKAO = 'https://pf.kakao.com/_eRvNX'
INSTAGRAM = 'https://www.instagram.com/guitin.official/'
EMAIL = 'guitin.official@gmail.com'
STIBEE = 'https://page.stibee.com/subscriptions/532247'
VERSION = '8'

ICON_MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 8h16M4 16h16"/></svg>'
ICON_CLOSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'
ICON_KAKAO = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 4C7 4 3 7.1 3 11c0 2.5 1.7 4.7 4.2 5.9l-.9 3.3c-.1.3.3.6.6.4l3.9-2.6c.4 0 .8.1 1.2.1 5 0 9-3.1 9-7S17 4 12 4z"/></svg>'




def head(title, desc, path, extra=''):
    url = SITE + path
    return f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GUITIN">
<meta property="og:locale" content="ko_KR">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F3EDE4">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/assets/img/icon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cardo:ital,wght@0,400;0,700;1,400&family=Noto+Serif+KR:wght@400;500&display=swap">
<link rel="stylesheet" href="/assets/css/site.css?v={VERSION}">
{extra}<script src="/assets/js/site.js?v={VERSION}" defer></script>
</head>
<body>
<a class="skip" href="#main">본문 바로가기</a>
'''


def header(current=''):
    def cur(name):
        return ' aria-current="page"' if current == name else ''
    return f'''<header class="site-header">
  <div class="wrap">
    <a class="logo" href="/" aria-label="GUITIN 홈">GUITIN</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="메뉴 열기">{ICON_MENU}</button>
    <nav class="nav" id="site-nav" aria-label="주 메뉴">
      <a href="/scents"{cur('scents')}>Scents</a>
      <a href="/story"{cur('story')}>Story</a>
      <a href="/shop"{cur('shop')}>Shop</a>
      <a class="btn btn--solid" href="#subscribe-section" data-subscribe>출시 소식 받기</a>
    </nav>
  </div>
</header>
'''


def form(fid, dark=False):
    """Email sign-up lives on Stibee's own page (it carries the consent boxes and reCAPTCHA)."""
    return f'''<div class="signup">
  <a class="btn btn--solid" href="{STIBEE}" target="_blank" rel="noopener">이메일로 출시 소식 받기</a>
  <p class="signup-note">스티비 구독 페이지가 새 창으로 열립니다. 수집 항목과 보관 기간은 <a href="/privacy">개인정보처리방침</a>에 있습니다.</p>
</div>'''


def dialog():
    return f'''<dialog class="modal" id="subscribe" aria-labelledby="subscribe-title">
  <div class="modal-card">
    <button class="modal-close" type="button" aria-label="닫기">{ICON_CLOSE}</button>
    <h2 id="subscribe-title">첫 번째 향의 출시 소식</h2>
    <p class="small">첫 제품은 산책 후 클렌징 티슈입니다. 출시 소식과 런칭 기념 쿠폰을 가장 먼저 보내드립니다.</p>
    <a class="btn btn--line" href="{KAKAO}" target="_blank" rel="noopener">{ICON_KAKAO}카카오톡으로 출시 소식 받기</a>
    <div class="divider">또는 이메일로</div>
    {form('dlg')}
  </div>
</dialog>
'''


def soldout_dialog():
    return f'''<dialog class="modal" id="soldout" aria-labelledby="soldout-title">
  <div class="modal-card">
    <button class="modal-close" type="button" aria-label="닫기">{ICON_CLOSE}</button>
    <span class="en-line" style="margin-top:0">Sold out</span>
    <h2 id="soldout-title">지금은 품절이에요</h2>
    <p class="small">첫 생산분을 준비하고 있어 아직 주문을 받지 않습니다. 주문은 접수되지 않았어요. 출시되면 가장 먼저 알려드릴까요?</p>
    <div class="modal-actions">
      <button class="btn btn--solid" type="button" data-go-subscribe>알림받기로 이동</button>
      <button class="btn btn--line" type="button" data-dismiss>닫기</button>
    </div>
  </div>
</dialog>
'''


def close(text):
    return f'''<section class="close on-dark" id="subscribe-section" aria-labelledby="close-title">
  <div class="wrap grid">
    <div>
      <h2 id="close-title">첫 번째 향의 출시 소식</h2>
      <span class="en-line">Be the first to smell it.</span>
      <p>{text}</p>
    </div>
    <div>
      {form('close', dark=True)}
      <div class="alt">
        <div class="divider" style="color:#CFC7B8">또는</div>
        <a class="btn btn--line" href="{KAKAO}" target="_blank" rel="noopener">{ICON_KAKAO}카카오톡으로 출시 소식 받기</a>
      </div>
    </div>
  </div>
</section>
'''


def footer():
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div>
      <div class="brand">GUITIN</div>
      <div class="brand-ko">귀탱 · 강아지를 위한 조향</div>
    </div>
    <ul>
      <li><a href="/scents">Scents</a></li>
      <li><a href="/story">Story</a></li>
      <li><a href="/shop">Shop</a></li>
      <li><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></li>
      <li><a href="{KAKAO}" target="_blank" rel="noopener">카카오톡 채널</a></li>
    </ul>
    <div class="meta">
      <a href="/privacy"><strong>개인정보처리방침</strong></a>
      <a href="/terms">이용약관</a>
      <span>문의 <a href="mailto:{EMAIL}">{EMAIL}</a></span>
      <span>© 2026 GUITIN</span>
    </div>
  </div>
</footer>
'''


def page(name, title, desc, path, body, current='', close_text=None):
    html = head(title, desc, path) + header(current) + '<main id="main">\n' + body
    if close_text:
        html += close(close_text)
    html += '</main>\n' + footer() + dialog() + soldout_dialog() + '</body>\n</html>\n'
    # version every image URL so a replaced picture is never served from an old browser cache
    import re
    html = re.sub(r'(/assets/img/[\w.-]+\.(?:webp|jpg|png))(?![\w?])', r'\1?v=' + VERSION, html)
    (ROOT / name).write_text(html, encoding='utf-8')
    print('wrote', name)


def pic(name, alt, widths, sizes, cls='', eager=False):
    """widths: list of (suffix, width); first is the largest."""
    srcset = ', '.join(f'/assets/img/{name}{s}.webp {w}w' for s, w in widths)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<img src="/assets/img/{name}{widths[0][0]}.webp" srcset="{srcset}" sizes="{sizes}" alt="{alt}" {load}{cls}>'


# ------------------------------------------------------------------ home
SCENES = [
    ('aw', 'I', '산책 후', '첫 제품', 'afterwalk', [('', 1400), ('-800', 800)],
     '견주 손바닥의 하얀 천 위에 올려놓은 강아지 앞발',
     '바깥 공기를 털어내고, 라벤더와 맑은 비누 향으로 숨을 고릅니다.', '/scents#after-walk', '산책 후 향 보기'),
    ('pd', 'II', '낮잠', '준비 중', 'pawppy', [('', 1400), ('-800', 800)],
     '햇볕 드는 담요 위에서 분홍 발바닥을 내밀고 자는 아기 강아지',
     '아기 강아지 배에서 나는 달콤한 꼬순내를 담았습니다.', '/scents#nap', '낮잠 향 보기'),
    ('cd', 'III', '목욕 후, 잠들기 전', '준비 중', 'cuddle', [('', 1122), ('-800', 800)],
     '노을빛 커튼 앞, 순면 이불 위에 엎드린 강아지의 뒷모습',
     '목욕을 마치고 이불 속에서 꼭 안고 잠드는 밤의 파우더리한 온기.', '/scents#night', '밤의 향 보기'),
]

scene_cards = '\n'.join(f'''      <a class="scene scene--{k}" href="{href}">
        <div class="scene-ph">{pic(img, alt, ws, '(max-width: 900px) 100vw, 33vw')}</div>
        <span class="scene-num">{num}</span>
        <h3>{when} <span class="status">{status}</span></h3>
        <p>{text}</p>
        <span class="go">{go}</span>
      </a>''' for k, num, when, status, img, ws, alt, text, href, go in SCENES)

home = f'''<section class="hero" aria-labelledby="hero-title">
  <picture>
    <source media="(max-width: 767px)" srcset="/assets/img/hero-mobile.webp">
    <img src="/assets/img/hero-pc.webp" srcset="/assets/img/hero-pc.webp 1672w, /assets/img/hero-pc-1100.webp 1100w" sizes="100vw" alt="창가 조향 작업대에서 시향지 끝에 코를 대는 귀탱이" fetchpriority="high">
  </picture>
  <div class="hero-copy" data-enter>
    <div class="hero-brand" aria-hidden="true">GUITIN</div>
    <div class="hero-tag">Perfumery for Dogs</div>
    <h1 id="hero-title">조향사가 만드는 강아지 향 케어</h1>
    <p>산책 후, 낮잠, 목욕 후. 강아지의 하루 세 순간에 맞춘 향을 조향사가 직접 설계합니다.</p>
    <div class="fact"><span>첫 제품</span><span>산책 후 클렌징 티슈</span><span>준비 중</span></div>
    <a class="btn btn--solid" href="#subscribe-section" data-subscribe>출시 소식 받기</a>
  </div>
</section>

<section class="section" aria-labelledby="scenes-title">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h-l" id="scenes-title">세 순간을 위한 세 가지 향<span class="en-line">Closer, through scent.</span></h2>
      <p class="lead">산책에서 돌아와 발을 닦는 시간, 햇볕 아래 낮잠, 목욕을 마치고 이불 속에서 잠드는 밤. 그 순간마다 강아지와 같은 향을 나눠 맡습니다.</p>
    </div>
    <div class="scenes">
{scene_cards}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="product-title">
  <div class="wrap product">
    <div class="product-art">{pic('lineup', 'GUITIN 클렌징 티슈, 샴푸, 미스트 스프레이 동판화 일러스트', [('', 1536), ('-900', 900)], '(max-width: 900px) 100vw, 55vw')}</div>
    <div class="product-copy">
      <h2 class="h-l" id="product-title">첫 제품, 산책 후 클렌징 티슈</h2>
      <p>산책에서 돌아와 현관에서 발과 몸을 닦는 향 클렌징 티슈입니다. 같은 향이 미스트와 샴푸로 이어집니다.</p>
      <ul class="product-list">
        <li><span class="k">향</span><span>라벤더, 맑은 비누, 포근한 머스크</span></li>
        <li><span class="k">쓰는 때</span><span>산책에서 돌아와 현관에서</span></li>
        <li><span class="k">성분</span><span>출시와 함께 전 성분 공개</span></li>
        <li><span class="k">출시</span><span>준비 중</span></li>
      </ul>
    </div>
  </div>
</section>
'''

page('index.html', 'GUITIN 귀탱 · 조향사가 만드는 강아지 향 케어',
     '산책 후, 낮잠, 목욕 후. 강아지의 하루 세 순간에 맞춘 향을 조향사가 설계합니다. 첫 제품은 산책 후 클렌징 티슈, 준비 중입니다.',
     '/', home, '', '첫 제품은 산책 후 클렌징 티슈입니다. 출시 소식과 런칭 기념 쿠폰을 가장 먼저 보내드립니다.')

# ------------------------------------------------------------------ scents
SCENTS = [
    ('aw', 'after-walk', 'I', '산책 후', '첫 제품', 'The moment you come home', 'afterwalk', [('', 1400), ('-800', 800)],
     '견주 손바닥의 하얀 천 위에 올려놓은 강아지 앞발',
     '현관문을 열자 바깥 공기가 따라 들어온다. 풀잎 내음, 서늘한 바람, 꼬리를 흔드는 강아지. 바닥에 앉아 네 발을 하나씩 닦아준다. 손끝에서 라벤더와 맑은 꽃비누 향이 번진다. 바깥의 공기가 천천히 물러나고, 부드러운 머스크가 털 사이에 남는다.',
     '산책의 끝을 맑게 정리하는 비누 꽃 향.',
     [('note-soap', '맑은 비누', '거품이 얹힌 비누 동판화'), ('note-lavender', '라벤더', '라벤더 가지 동판화'), ('note-cotton', '포근한 머스크', '목화솜 동판화')],
     '산책에서 돌아와 현관에서. 향을 머금은 클렌징 티슈로 발과 몸을 닦아주며.'),
    ('pd', 'nap', 'II', '낮잠', '준비 중', 'The nap in the sun', 'pawppy', [('', 1400), ('-800', 800)],
     '햇볕 드는 담요 위에서 분홍 발바닥을 내밀고 자는 아기 강아지',
     '바닥에 햇빛이 네모나게 놓여 있다. 강아지는 그 안에 배를 드러내고 누워, 꿈을 꾸는지 발끝을 작게 움직인다. 따뜻해진 배에 코를 대자, 어릴 적 우유 한 잔과 코코아 같은 달콤한 것이 올라온다.',
     '아기 강아지 배의 꼬순내를 닮은 구아망드.',
     [('note-milk', '따뜻한 우유', '우유 주전자 동판화'), ('note-cereal', '코코아 시리얼', '시리얼 그릇 동판화'), ('note-paw', '아기 강아지 발바닥', '니트 속 강아지 발바닥 동판화')],
     '낮잠에서 깨어난 후, 또는 안아줄 때.'),
    ('cd', 'night', 'III', '목욕 후, 잠들기 전', '준비 중', 'The night under the duvet', 'cuddle', [('', 1122), ('-800', 800)],
     '노을빛 커튼 앞, 순면 이불 위에 엎드린 강아지의 뒷모습',
     '목욕을 마친 털이 아직 조금 따뜻하다. 구겨진 흰 이불 속에 강아지가 먼저 파묻힌다. 팔을 두르자 등을 기대오는 무게. 오늘 하루가 여기서 끝난다.',
     '폭닥한 이불과 온기를 담은, 짙은 파우더리 향.',
     [('note-powder', '파우더', '파우더 퍼프 동판화'), ('note-cedar', '포근한 우디', '삼나무 가지 동판화'), ('note-cashmere', '살결 머스크', '캐시미어 천 동판화')],
     '목욕 후, 잠들기 전 마지막 순서로.'),
]

scent_sections = '\n'.join(f'''<section class="scent scent--{k}" id="{sid}" aria-labelledby="{sid}-title">
  <div class="wrap">
    <div class="scent-ph">{pic(img, alt, ws, '(max-width: 900px) 100vw, 50vw')}</div>
    <div class="scent-txt">
      <span class="num">{num}</span>
      <h2 class="h-l" id="{sid}-title">{when} <span class="status">{status}</span><span class="en-line">{en}</span></h2>
      <p class="story">{story}</p>
      <p class="line">{line}</p>
      <ul class="notes">
{chr(10).join(f'        <li><img src="/assets/img/{n}.webp" alt="{nalt}" width="420" height="420" loading="lazy" decoding="async"><span>{nl}</span></li>' for n, nl, nalt in notes)}
      </ul>
      <p class="use">쓰는 순간 — {use}</p>
    </div>
  </div>
</section>''' for k, sid, num, when, status, en, img, ws, alt, story, line, notes, use in SCENTS)

scents = f'''<section class="intro">
  <div class="wrap">
    <h1 class="h-xl">강아지의 하루에서 나온 세 가지 향<span class="en-line">A day with three scents.</span></h1>
    <p class="lead">산책에서 돌아온 현관, 햇볕 드는 낮잠, 이불 속의 밤. 순간에 어울리는 향을 강아지와 사람을 위해 만듭니다. 하나의 향은 티슈에서 시작해 미스트와 샴푸로 이어집니다.</p>
  </div>
</section>
<div class="lineup"><div class="wrap">{pic('lineup', 'GUITIN 클렌징 티슈, 샴푸, 미스트 스프레이 동판화 일러스트', [('', 1536), ('-900', 900)], '(max-width: 1100px) 100vw, 1040px')}</div></div>
{scent_sections}
<section class="promise">
  <div class="wrap"><p>GUITIN은 모든 향의 전 성분을 공개합니다.</p></div>
</section>
'''

page('scents.html', '세 가지 향 · GUITIN 귀탱',
     '산책 후, 낮잠, 목욕 후 잠들기 전. 강아지의 하루 세 순간을 위한 GUITIN의 세 가지 향과 향 노트를 소개합니다.',
     '/scents', scents, 'scents', '첫 번째 향은 산책 후의 향, 클렌징 티슈로 먼저 선보입니다. 출시 소식과 런칭 기념 쿠폰을 가장 먼저 보내드립니다.')

# ------------------------------------------------------------------ story
story = f'''<section class="intro">
  <div class="wrap">
    <h1 class="h-xl">귀탱이에서 시작한 브랜드<span class="en-line">It began with one dog.</span></h1>
    <p class="lead">한 마리 강아지에서 시작했습니다. GUITIN의 모든 향은 귀탱이의 코를 먼저 지나갑니다.</p>
  </div>
</section>

<section class="dog" aria-labelledby="guitang-title">
  <div class="wrap">
    <div class="dog-ph">{pic('guitang', '모란 정원 길에 앉아 눈을 감고 활짝 웃는 귀탱이 동판화 일러스트', [('', 1000), ('-700', 700)], '(max-width: 900px) 100vw, 45vw')}</div>
    <div class="dog-txt">
      <h2 class="h-l" id="guitang-title">귀탱이</h2>
      <p class="role">CNO — Chief Nose Officer</p>
      <p>귀탱이는 미니어처 오스트레일리안 셰퍼드입니다. 검정과 흰색, 그리고 황금빛 탄. 한쪽 귀에만 흰 점이 있고, 한쪽 눈 위에만 금색 눈썹이 있습니다. 완벽하게 대칭이 아니어서 더 오래 들여다보게 되는 얼굴입니다.</p>
      <p>산책을 나가면 귀탱이는 걷기보다 냄새 맡기에 바쁩니다. 풀숲에도, 담벼락에도, 바람이 지나간 자리에도 코를 대봅니다. 마음에 드는 냄새를 찾으면 그 위에 몸을 부비며 한참을 떠나지 않습니다. 귀탱이의 취향은 대개 젖은 흙과 풀밭입니다.</p>
      <p>귀탱이가 좋아하는 냄새와 사람이 좋아하는 향은 조금 다릅니다. GUITIN은 그 사이를 조향합니다. 귀탱이가 고개를 돌리지 않고, 곁에 있는 사람도 기분이 좋아지는 향. 둘이 조금 더 가까이 붙어 있고 싶어지는 향을 만듭니다.</p>
    </div>
  </div>
</section>

<section class="dog dog--b" aria-labelledby="butter-title">
  <div class="wrap">
    <div class="dog-ph">{pic('butter', '정원 잔디에 엎드려 옆을 바라보는 버터 동판화 일러스트', [('', 1000), ('-700', 700)], '(max-width: 900px) 100vw, 45vw')}</div>
    <div class="dog-txt">
      <h2 class="h-l" id="butter-title">버터</h2>
      <p class="role">Head of Security · 보안과장</p>
      <p>버터는 길에서 온 아이입니다. 하얗고 부드러운 털에 베이지색 귀, 풍성한 꼬리와 긴 다리. 눈은 가장자리가 호박색이고 안쪽으로 갈수록 그레이빛이 번집니다. 코와 발바닥과 배는 모두 분홍색입니다.</p>
      <p>버터가 좋아하는 일은 순찰입니다. 산책길마다 빠짐없이 한 바퀴를 돕니다. 골목 모퉁이, 가로수, 전봇대까지 하나하나 들러 오늘도 이상 없음을 확인합니다. 귀탱이가 향을 고르는 동안, 버터는 아틀리에를 지킵니다.</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="standards-title">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h-l" id="standards-title">GUITIN이 지키는 네 가지<span class="en-line">What we stand by.</span></h2>
    </div>
    <div class="standards">
      <div class="standard"><span class="n">I</span><h3>조향사가 직접 설계한 향</h3><p>향 하나에 장면 하나. 강아지의 하루에서 출발해 하나씩 구성합니다.</p></div>
      <div class="standard"><span class="n">II</span><h3>사람도 함께 맡고 싶은 향</h3><p>있는 듯 없는 향이 아니라, 안아줄 때마다 다시 느껴지는 향. 코끝을 찌르지 않고 털결에 가까이 머물도록 만듭니다.</p></div>
      <div class="standard"><span class="n">III</span><h3>귀탱이가 먼저 고른 원료</h3><p>모든 원료는 귀탱이가 가장 먼저 맡습니다. 고개를 돌리는 원료는 빼고, 코를 가까이 대는 원료만 남깁니다.</p></div>
      <div class="standard"><span class="n">IV</span><h3>숨기지 않는 향</h3><p>강아지의 몸에 닿는 것이기에, 전 성분을 공개합니다.</p></div>
    </div>
  </div>
</section>
'''

page('story.html', '이야기 · GUITIN 귀탱',
     '미니어처 오스트레일리안 셰퍼드 귀탱이에서 시작한 강아지 향 브랜드 GUITIN의 이야기와 네 가지 원칙.',
     '/story', story, 'story', '귀탱이가 고른 첫 번째 향은 산책 후의 클렌징 티슈로 찾아옵니다. 출시 소식과 런칭 기념 쿠폰을 가장 먼저 보내드립니다.')

# ------------------------------------------------------------------ shop
shop = f'''<section class="shop" aria-labelledby="shop-title">
  <div class="wrap shop-grid">
    <div class="shop-art">
      <div class="shop-ph">{pic('lineup', 'GUITIN 클렌징 티슈, 샴푸, 미스트 스프레이 동판화 일러스트', [('', 1536), ('-900', 900)], '(max-width: 900px) 100vw, 55vw', eager=True)}</div>
      <p class="small">이미지는 일러스트입니다. 실제 제품 사진은 출시 때 공개합니다.</p>
    </div>
    <div class="shop-info">
      <span class="num">I · 산책 후</span>
      <h1 class="h-l" id="shop-title">산책 후 클렌징 티슈 <span class="status status--out">품절</span><span class="en-line">After the walk.</span></h1>
      <p>산책에서 돌아와 현관에서 발과 몸을 닦는 향 클렌징 티슈. 라벤더와 맑은 비누 향으로 바깥 공기를 정리하고, 포근한 머스크가 털 사이에 남습니다.</p>
      <p class="price"><span class="k">가격</span><span>출시 때 공개</span></p>
      <ul class="product-list">
        <li><span class="k">향</span><span>라벤더, 맑은 비누, 포근한 머스크</span></li>
        <li><span class="k">구성</span><span>60매 · 캡형</span></li>
        <li><span class="k">쓰는 때</span><span>산책에서 돌아와 현관에서</span></li>
        <li><span class="k">성분</span><span>출시와 함께 전 성분 공개</span></li>
      </ul>
      <div class="buy">
        <div class="qty" role="group" aria-label="수량">
          <button type="button" data-qty="-1" aria-label="수량 빼기">−</button>
          <output id="qty" aria-live="polite">1</output>
          <button type="button" data-qty="1" aria-label="수량 더하기">+</button>
        </div>
        <button class="btn btn--solid buy-btn" type="button" data-soldout>주문하기</button>
      </div>
      <p class="small">현재 품절입니다. 주문하기를 누르면 출시 알림을 신청할 수 있어요.</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="next-title">
  <div class="wrap">
    <div class="section-head">
      <h2 class="h-m" id="next-title">다음 향<span class="en-line">Coming next.</span></h2>
    </div>
    <ul class="next-list">
      <li><span class="num">II</span><span>낮잠</span><span class="status">준비 중</span><a class="textlink" href="/scents#nap">향 보기</a></li>
      <li><span class="num">III</span><span>목욕 후, 잠들기 전</span><span class="status">준비 중</span><a class="textlink" href="/scents#night">향 보기</a></li>
    </ul>
  </div>
</section>
'''

page('shop.html', '주문하기 · GUITIN 귀탱',
     'GUITIN 첫 제품, 산책 후 클렌징 티슈. 현재 품절이며 출시 알림을 신청할 수 있습니다.',
     '/shop', shop, 'shop', '첫 제품은 산책 후 클렌징 티슈입니다. 출시 소식과 런칭 기념 쿠폰을 가장 먼저 보내드립니다.')

# ------------------------------------------------------------------ legal + 404
legal_src = (ROOT / '_src')
page('privacy.html', '개인정보처리방침 · GUITIN', 'GUITIN(귀탱) 개인정보처리방침', '/privacy',
     (legal_src / 'privacy.part.html').read_text(encoding='utf-8'))
page('terms.html', '이용약관 · GUITIN', 'GUITIN(귀탱) 웹사이트 이용약관', '/terms',
     (legal_src / 'terms.part.html').read_text(encoding='utf-8'))
page('404.html', '페이지를 찾을 수 없습니다 · GUITIN', '요청한 페이지를 찾을 수 없습니다.', '/404', '''<section class="notfound">
  <div class="wrap">
    <h1 class="h-l">페이지를 찾을 수 없습니다</h1>
    <p>주소가 바뀌었거나 없는 페이지입니다. 귀탱이도 이 냄새는 처음 맡아봅니다.</p>
    <a class="btn btn--solid" href="/">홈으로 가기</a>
  </div>
</section>
''')
