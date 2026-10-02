# -*- coding: utf-8 -*-
"""Merge other-AI strengths into material schedule → Rev.1."""
from __future__ import annotations

from pathlib import Path

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

SRC = Path(r"c:\Users\Rico\Downloads\Material_Schedule_HK_36sqm_Final.xlsx")
OUTS = [
    Path(r"c:\Users\Rico\Downloads\Material_Schedule_HK_36sqm_Final_Rev1.xlsx"),
    Path(r"c:\Users\Rico\PycharmProjects\Skills-Architects-HK\.tmp_tender_pages\Material_Schedule_HK_36sqm_Final_Rev1.xlsx"),
]

# col index 1-based matching HEADERS
# 1物料項目 2類別 3編碼 4區域 5品牌 6型號 7尺寸 8表面 9內籠 10五金 11收口 12數量 13圖樣 14採購 15供應商 16網址 17陪同 18備註

PATCHES: dict[str, dict[int, str]] = {
    # bathroom floor — R10/R11 + adhesive brands
    "FL-02": {
        7: "600×300mm；厚約9–10mm；吸水率E≤0.5%；濕態防滑不低於R10，淋浴／易積水宜達R11（DIN 51130或同等）；預留損耗≥5%；接縫2–3mm",
        11: "向地漏找坡及自排水；與牆磚C同廠；門口接吸咀F；須提交濕態防滑測試資料",
        18: "瓷磚膠／防霉填縫：Mapei、ARDEX或Bostik同等級，按基層及磚吸水率選膠；備選金銀倉https://www.shknw.com/index.php?path=108&route=product%2Fcategory",
    },
    "FL-03": {
        7: "600×300mm；厚約9–10mm；吸水率E≤0.5%；防滑約R10；預留損耗≥5%；接縫2–3mm",
        18: "瓷磚膠：Mapei／ARDEX／Bostik或同等；與FL-02同一次訂貨減色差",
    },
    "FL-01": {
        11: "與吸咀F平口／金屬收邊；乾區腳線80mm；清拆舊磚後找平＋防潮膜；色差現場對燈核色；預留損耗≥5%",
        18: "備選Quick-Step：https://int.quick-step.com/en；主選維持圖則SPC石塑（非全瓷磚）",
    },
    "TH-01": {
        7: "厚20mm；闊度≥門扇＋兩邊各約20mm；長度現場度尺；前緣倒角3–5mm",
        11: "兩側與SPC／瓷磚平口或微凸；底塗＋中性矽酮膠／防霉膠；邊位倒角",
    },
    "WS-01": {
        7: "厚20mm；深度依現有窗臺（約600mm級，現場覆核）；滿鋪；前緣倒角3–5mm",
        11: "周邊中性防霉矽酮膠；與窗框／牆身收口；石材背面及接縫防污防水；天然石若採用須先做防護劑",
        18: "盡量與TH-01、CT-B1同一石廠；優先石英石減保養（圖則允許雲石／石英石）",
    },
    "WT-A": {
        7: "600×300mm；厚約8–10mm；低吸水率",
        11: "鋪至鋁天花底；陰陽角同色收口條或45°碰角",
        18: "與FL-03同廠線；瓷磚膠Mapei／ARDEX／Bostik或同等",
    },
    "WT-B": {
        11: "與枱面H、吊櫃收口；爐後位置不採用未經防火及耐熱確認的木飾面",
        18: "薩米特：https://echouse.com.hk/decoration_strategy/summit-ceramic-tiles-hong-kong-exclusive-ecmall/；膠泥同上",
    },
    "WT-C": {
        7: "600×300mm；厚約8–10mm；低吸水率；啞光或半啞面",
        11: "滿高至鋁天花；與地磚D對縫；陰陽角同色收口條或45°碰角",
        18: "濕區用防霉填縫劑；膠泥Mapei／ARDEX／Bostik或同等",
    },
    "WT-D": {
        11: "淋浴區加強防水後貼磚；陰陽角收口條",
        18: "防滑區／淋浴背牆宜配合R10–R11地磚策略",
    },
    "WP-01": {
        5: "Sika／Mapei／ARDEX／Bostik（或同等）",
        6: "SikaTop-107 Seal HK＋SikaLatex 700；或Mapei Mapelastic；或ARDEX／Bostik濕區系統",
        11: "鋪磚前強制蓄水試驗；陰陽角加強網；所有切口、螺絲孔、喉管穿板位須防水封邊",
        18: "與瓷磚膠系統盡量同一品牌系列，按廠方說明施工",
    },
    "CT-H": {
        7: "厚12mm（圖則Corian H）；長度現場度尺；無縫駁口；前緣倒角或小圓角3–5mm",
        11: "靠牆防霉矽酮膠或薄上翻；水槽及爐具開孔現場覆核；爐邊須墊耐熱墊，不可空燒石面",
        18: "維持圖則人造石Corian；若改20mm石英石須先改圖再招標。備選Lexton／Staron：http://mail.lexton.com.hk/",
    },
    "CT-B1": {
        7: "厚20mm石英石（或Corian 12mm）；闊配B1櫃；前緣倒角3–5mm",
        11: "盆周防霉矽酮膠；背後靠牆收口；水喉穿板位封膠",
    },
    "CB-HPL": {
        8: "防火／耐火級HPL 0.8–1.0mm（需時選FR）；見光位同色封邊",
        9: "貼於18mm E1（或同等低甲醛）防潮夾板門板／側板",
        18: "供應商須提交甲醛測試（EN 13986 E1／GB 18580／F☆☆☆☆或同等）。備選LAMITAK／Wilsonart見原連結",
    },
    "CB-PLY": {
        5: "優質夾板 E1／E0（或同等低甲醛）",
        6: "18mm防潮夾板；廚房／浴室優先HMR（High Moisture Resistant）板",
        9: "內籠18mm夾板；內面宜貼0.6mm白色HPL；背板不少於6–9mm",
        11: "濕區櫃底升高／防潮踢腳；水槽櫃內加防水盤；切口、邊位、螺絲孔、穿喉位防水封邊；見光面封ABS／PVC邊條",
        18: "禁止未封邊刨花板；須提交低甲醛測試報告。K2可用針葉夾板＋耐火板",
    },
    "HW-01": {
        6: "Clip top緩衝鉸；TANDEMBOX／LEGRABOX全拉出式緩衝路軌（木廠選配）；承重滑軌用於床下抽屜",
        10: "緩衝鉸、全拉出緩衝路軌、衣通、層板釘；B1暗抽手；床下抽屜加防傾倒裝置",
        18: "可同等Hettich https://www.hettich.com/；固定件須固定於結構牆或加強底板",
    },
    "HW-S1": {
        8: "噴粉啞光（粉末塗層，避免普通噴漆剝落）",
        5: "訂造鋁合金或不鏽鋼304噴粉架",
        18: "濕區外金屬件仍建議防鏽處理；色跟全屋金屬統一啞黑或香檳",
    },
    "HW-B2": {
        5: "不鏽鋼304或鋁合金（訂造）",
        8: "髮絲或粉末噴塗；鏡面",
        11: "鏡邊密封防潮；固定點防水密封；濕區禁止普通鐵件",
        18: "配防水LED；玻璃須鋼化及磨邊",
    },
    "CL-01": {
        7: "板寬300mm（對齊圖則）；鋁板厚度不少於0.6mm；RAL白／淺灰",
        9: "防鏽鋁龍骨／隱藏式或條板龍骨系統",
        11: "可拆面板方便檢修喉電；接縫及邊位平直；周邊收邊條",
        18: "維持300闊鋁條（非600方板lay-in），除非改圖",
    },
    "CL-02": {
        5: "Knauf／Gyproc（或同等）石膏板系統",
        6: "9.5mm或12.5mm防潮石膏板，符合BS EN 520（或同等）；金屬鍍鋅龍骨",
        8: "接縫填料及紙帶處理後髹水性乳膠漆；燈槽木殼可油漆木紋",
        11: "與樑／原天花交接；預留冷氣喉位；燈槽滲光構造；電源供應器須可維修",
        18: "FS Code相關石膏板要求可參考BS EN 520；燈槽不可封死檢修",
    },
    "PT-01": {
        6: "超耐洗／淨味系列（待選色號）；底漆1層＋面漆2層；啞光或蛋殼光",
        8: "水性低VOC內牆乳膠漆；抗鹼、防霉",
        11: "濕區天花加防霉；須提供VOC資料及SDS安全資料表",
        18: "備選立邦／Jotun或同等；符合香港建築漆料VOC管制要求",
    },
    "PT-02": {
        9: "按廠方底塗系統；基材宜E1夾板（若有木基層）",
        18: "與PT-01色系協調；木基材須低甲醛證明",
    },
    "DR-FD": {
        11: "須附FD120測試報告／認證門組；核屋苑及消防分隔要求；不可只按外觀選材",
        10: "防火鉸、閉門器、防火鎖等配套（認證配件）",
        18: "備選https://www.ulsteel.com.hk/fire_rated_steel_door_transformer_room_door/；涉及改廚須核BD／管理處",
    },
    "DR-B": {
        10: "緩衝／靜音門鉸；門底通風百葉；304不鏽鋼或鋅合金鎖具（髮絲／啞黑）",
        11: "更換門框；與磚牆收口；現場覆核垂直度及門隙",
    },
    "DR-01": {
        10: "緩衝／靜音門鉸、磁吸或機械門鎖、門吸；304不鏽鋼或鋅合金；指定髮絲／啞黑",
        11: "全屋內門框扇更換；現場覆核垂直度及門隙",
        6: "實心夾板門或E1級木門；表面HPL、木皮或噴漆",
    },
    "SW-05": {
        7: "鋼化清玻厚8–10mm；半身高；高度按P6；四邊磨邊",
        11: "底部坐缸邊防水；固定方式及安全間隙由玻璃商核對；不可用未鋼化玻璃",
        5: "訂造鋼化玻璃＋金屬框（304／鋁合金）",
    },
    "LG-01": {
        7: "軌道長度按P3；燈具約7–9W級；3000K；CRI≥90；建議深防眩／低眩光；PF≥0.9",
        18: "光通量參考約500–700 lm／模組（按選型）；3000K全屋統一",
    },
    "LG-02": {
        6: "24V燈帶；約9.6–14.4 W/m；3000K；CRI≥90；乾區IP20；濕區燈槽建議IP65",
        11: "鋁槽＋乳白擴散罩；電源供應器須可維修；不可直接裸露安裝燈帶",
        18: "驅動器預留檢修口",
    },
    "LG-03": {
        6: "5–9W嵌入式LED；IP44或以上；3000K；CRI≥90；PF≥0.9",
        11: "配鋁天花裁孔；淋浴區內燈具IP等級須按實際位置及電氣規範確認",
        18: "另有5W氣氛小筒燈按圖；光通量參考約500–700 lm",
    },
}

NEW_ROWS: list[list[str]] = [
    [
        "瓷磚膠及防霉填縫劑",
        "鋪貼輔材",
        "AD-01",
        "浴室／廚房牆地磚鋪貼",
        "Mapei／ARDEX／Bostik（或同等）",
        "按磚材吸水率及基層選用濕區瓷磚膠＋防霉填縫劑",
        "按廠方用量；接縫2–3mm",
        "—",
        "—",
        "—",
        "與防水系統兼容；按廠方養護期後才浸水／使用",
        "按鋪磚面積計",
        "P2；P6；P7",
        "建材行／經泥水採購",
        "經承造商或品牌經銷",
        "https://hkg.sika.com/zh/distribution-retail/household_waterproofing/kitchen_and_bathroom.html",
        "否",
        "Rev.1併入：對方建議之膠泥品牌要求",
    ],
    [
        "櫃門／展示玻璃",
        "玻璃",
        "GL-01",
        "廚櫃磨砂玻璃門、展示櫃等（按圖）",
        "訂造鋼化玻璃",
        "6mm鋼化透明／灰玻／茶玻／磨砂；高身玻璃門可8mm；四邊磨邊",
        "按門扇分格現場度尺",
        "磨邊；指定透明度／磨砂",
        "—",
        "緩衝鉸鏈或鋁框；不可用未鋼化玻璃",
        "玻璃不可直接承受櫃體荷載；尺寸、厚度、固定及安全間隙由供應商核對",
        "按圖門扇數",
        "P1；P7（磨砂玻璃）",
        "玻璃廠訂造",
        "經承造商",
        "—",
        "是",
        "Rev.1併入：對方G1玻璃安全規格",
    ],
    [
        "金屬框／收口條",
        "金屬配件",
        "MT-01",
        "全屋鋁條、收口、電視牆裝飾鋁條、浴屏框等",
        "鋁合金或不鏽鋼304",
        "指定粉末噴塗色（啞黑或香檳，全屋統一）",
        "厚度按跨度及荷載計算；裝飾鋁條約10–20mm級（按立面）",
        "粉末噴塗或PVDF；避免普通噴漆剝落",
        "—",
        "防鏽固定件",
        "濕區優先304／鋁合金；固定點防水密封",
        "按圖延米／件",
        "P4–P7",
        "金屬廠／經承造",
        "經承造商",
        "—",
        "是（選色）",
        "Rev.1併入：對方M1金屬規格；全屋只選一款金屬色",
    ],
    [
        "房門五金套裝",
        "五金",
        "DH-01",
        "所有內門（不含防火門認證配件）",
        "304不鏽鋼或鋅合金",
        "門鎖、門鉸、門吸；指定髮絲／啞黑",
        "按門扇厚度及洞口",
        "髮絲或啞黑",
        "—",
        "靜音門鉸、門鎖、門吸",
        "防火門須用認證防火五金（見DR-FD）；現場覆核門隙及垂直度",
        "按門樘數",
        "設計圖；P6；P7",
        "五金行／木廠統包",
        "經承造商",
        "—",
        "可選",
        "Rev.1併入：對方D2",
    ],
    [
        "冷氣機位／包封",
        "機電包封",
        "AC-01",
        "客廳／睡房分體冷氣機位及喉碼包封",
        "防潮夾板或鋁板",
        "12–18mm防潮夾板或鋁板包封",
        "按空調機型及現場",
        "外飾HPL／油漆／鋁板按設計",
        "防潮夾板；可拆檢修口",
        "通風百葉；可拆面板鉸／磁吸",
        "不可封死回風及維修位；按冷氣品牌散熱及排水要求確認；預留排水／除濕檢修空間",
        "按實際機位（暫估1–2處）",
        "P4；P5立面冷氣位",
        "木廠／鋁工程經承造",
        "經承造商",
        "—",
        "否",
        "Rev.1併入：對方AC1；與床架／櫃體保留檢修空間",
    ],
    [
        "木飾面牆／木格柵",
        "牆身飾面",
        "WD-01",
        "客廳電視牆木格柵等",
        "工程木皮／實木皮（或同等）",
        "12–18mm E1夾板基底＋木皮或水性噴漆；格柵間距按立面",
        "按P4立面",
        "啞光清漆或指定木皮色",
        "E1夾板或防潮夾板（避免普通MDF於潮濕環境）",
        "可配裝飾鋁條（見MT-01）",
        "固定於結構牆或加強底板；背後預留伸縮及LED檢修空間；長條件防翹曲",
        "約1面牆（現場計）",
        "P4 電視牆立面",
        "木廠訂造",
        "經承造木廠",
        "—",
        "是",
        "Rev.1併入：對方W3／W4；須提交甲醛測試",
    ],
]

GENERAL_NOTES = [
    ["序號", "總則 General Notes（Rev.1 併入）"],
    ["1", "所有材料、顏色、紋理、邊口及五金須先提交實物樣板、產品資料及施工樣板，經設計方批准後方可訂購及施工。"],
    ["2", "所有尺寸均須由承建商現場覆核。圖則尺寸只作設計及報價參考，不能代替現場量度。"],
    ["3", "所有木板、夾板、MDF、刨花板及櫃體基材須為低甲醛產品，最少符合E1級或同等（EN 13986 E1／GB 18580／Japan F☆☆☆☆等）；供應商須提交測試報告。香港潮濕環境：濕區優先防潮夾板／HMR，慎用普通MDF。"],
    ["4", "所有室內油漆、膠水、填縫劑及密封膠須採用低VOC產品；須提供VOC資料及SDS。香港室內空氣質素指引建議使用低排放材料，並要求供應商提供國際測試或環保認證。"],
    ["5", "廚房、浴室及所有可能接觸水的位置，櫃體應使用防潮夾板或HMR板；水槽櫃加防水盤；所有切口、邊位、螺絲孔及喉管穿板位須作防水封邊。"],
    ["6", "浴室地磚須提交濕態防滑測試資料（DIN 51130或同等）。一般濕區至少R10，淋浴及易積水位置宜考慮R11；並配合找坡排水設計。"],
    ["7", "所有浴室／廚房牆地磚須使用適合濕區的瓷磚膠及防霉填縫劑（Mapei、ARDEX、Bostik或同等），並按基層及磚材吸水率選擇膠泥。"],
    ["8", "玻璃須為鋼化玻璃；浴室玻璃、櫃門玻璃及高位玻璃須磨邊。玻璃尺寸、厚度、固定方式及安全間隙由供應商核對；玻璃不可直接承受櫃體荷載。"],
    ["9", "所有金屬材料須具防鏽處理；浴室及廚房優先使用304不鏽鋼、鋁合金或熱浸鍍鋅；黑色表面宜粉末噴塗或PVDF。全屋金屬色統一（啞黑或香檳擇一）。"],
    ["10", "如工程涉及改動廚房、浴室、分間牆、消防分隔或其他大廈設施，須按屋苑管理處、註冊承建商及屋宇署要求核對，並符合《建築物條例》及消防、結構等要求。廚房防火門維持圖則FD120認證門組。"],
    ["11", "主選材維持圖則：客飯廳／睡房為SPC石塑地板（非擅自改全瓷磚）；廚枱為Corian人造石H（非擅自改石英除非改圖）；廚／浴天花為300闊鋁條（非擅自改600方板）。"],
    ["12", "燈具色溫建議全屋3000K，CRI≥90；燈帶採24V並預留驅動器檢修；筒燈濕區IP44或以上。"],
    ["13", "版本：Material Schedule HK 36sqm Final Rev.1｜合併對方AI之性能規格／總則／漏項，保留本圖則主選材。"],
]


def style_row(ws, r_idx: int, zebra: PatternFill, cell_font: Font, wrap: Alignment, thin: Border) -> None:
    for c_idx in range(1, 19):
        cell = ws.cell(r_idx, c_idx)
        cell.font = cell_font
        cell.alignment = wrap
        cell.border = thin
        if r_idx % 2 == 0:
            cell.fill = zebra


def main() -> None:
    wb = load_workbook(SRC)
    ws = wb["物料規格表"]

    # map item code -> row
    code_col = 3
    code_to_row: dict[str, int] = {}
    for r in range(2, ws.max_row + 1):
        code = ws.cell(r, code_col).value
        if code:
            code_to_row[str(code)] = r

    for code, fields in PATCHES.items():
        r = code_to_row.get(code)
        if not r:
            raise SystemExit(f"missing code {code}")
        for c, val in fields.items():
            ws.cell(r, c).value = val

    cell_font = Font(name="Microsoft YaHei", size=9)
    wrap = Alignment(wrap_text=True, vertical="top")
    thin = Border(
        left=Side(style="thin", color="B0B0B0"),
        right=Side(style="thin", color="B0B0B0"),
        top=Side(style="thin", color="B0B0B0"),
        bottom=Side(style="thin", color="B0B0B0"),
    )
    zebra = PatternFill("solid", fgColor="F2F2F2")
    new_fill = PatternFill("solid", fgColor="E2EFDA")  # mark Rev.1 new rows

    start = ws.max_row + 1
    for i, row in enumerate(NEW_ROWS):
        r_idx = start + i
        assert len(row) == 18
        for c_idx, val in enumerate(row, 1):
            cell = ws.cell(r_idx, c_idx, val)
            cell.font = cell_font
            cell.alignment = wrap
            cell.border = thin
            cell.fill = new_fill
        ws.row_dimensions[r_idx].height = 55

    ws.auto_filter.ref = f"A1:R{ws.max_row}"

    # replace notes sheet
    if "填表說明" in wb.sheetnames:
        del wb["填表說明"]
    if "總則GeneralNotes" in wb.sheetnames:
        del wb["總則GeneralNotes"]

    ws_notes = wb.create_sheet("填表說明", 1)
    intro = [
        ["欄位", "說明"],
        ["編碼(Item no.)", "對應圖紙物料代號（FL／WT／CT／CB／SW等）；Rev.1新增AD／GL／MT／DH／AC／WD"],
        ["綠色底列", "Rev.1新增加入之項目（對方優點併入）"],
        ["品牌／型號", "已填建議首選；「待選」須設計師陪同展廳落實"],
        ["數量或單位", "約36m²暫估，招標前現場覆核"],
        ["圖樣", "tender PDF：P2地板、P3天花、P4–P7立面"],
        ["版本", "Rev.1｜合併性能規格、總則、漏項；主選材維持圖則"],
    ]
    for r, row in enumerate(intro, 1):
        for c, v in enumerate(row, 1):
            cell = ws_notes.cell(r, c, v)
            cell.font = Font(name="Microsoft YaHei", size=10, bold=(r == 1))
            cell.alignment = wrap
    ws_notes.column_dimensions["A"].width = 18
    ws_notes.column_dimensions["B"].width = 88

    ws_gn = wb.create_sheet("總則GeneralNotes", 2)
    header_fill = PatternFill("solid", fgColor="1F4E79")
    for r, row in enumerate(GENERAL_NOTES, 1):
        for c, v in enumerate(row, 1):
            cell = ws_gn.cell(r, c, v)
            cell.font = Font(
                name="Microsoft YaHei",
                size=10,
                bold=(r == 1),
                color="FFFFFF" if r == 1 else "000000",
            )
            cell.alignment = wrap
            if r == 1:
                cell.fill = header_fill
            cell.border = thin
        ws_gn.row_dimensions[r].height = 36 if r > 1 else 22
    ws_gn.column_dimensions["A"].width = 8
    ws_gn.column_dimensions["B"].width = 100

    # bump version remark on first data row note area - add sheet header title via freeze remains
    for p in OUTS:
        wb.save(p)
        print("saved", p.name, "bytes", p.stat().st_size, "rows", ws.max_row - 1)


if __name__ == "__main__":
    main()
