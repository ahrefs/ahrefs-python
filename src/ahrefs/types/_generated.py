# AUTO-GENERATED -- DO NOT EDIT

# ruff: noqa: E501

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from ahrefs.types._coercions import DateStr, SelectStr


class AggregationEnum(StrEnum):
    SIMILAR_LINKS = "similar_links"
    _1_PER_DOMAIN = "1_per_domain"
    ALL = "all"


class BestPositionKindEnum(StrEnum):
    PAID_TOP = "paid_top"
    PAID_BOTTOM = "paid_bottom"
    PAID_RIGHT = "paid_right"
    PAID_SITELINK = "paid_sitelink"
    ORGANIC = "organic"
    SITELINK = "sitelink"
    SNIPPET = "snippet"
    IMAGE = "image"
    ARTICLE = "article"
    KNOWLEDGE_CARD = "knowledge_card"
    KNOWLEDGE_PANEL = "knowledge_panel"
    LOCAL_PACK = "local_pack"
    LOCAL_TEASER = "local_teaser"
    NEWS = "news"
    QUESTION = "question"
    REVIEW = "review"
    SHOPPING = "shopping"
    TWEET = "tweet"
    SPELLING = "spelling"
    VIDEO = "video"
    DISCUSSION = "discussion"
    AI_OVERVIEW = "ai_overview"
    AI_OVERVIEW_SITELINK = "ai_overview_sitelink"
    ORGANIC_SHOPPING = "organic_shopping"


class BestPositionSetEnum(StrEnum):
    TOP_3 = "top_3"
    TOP_4_10 = "top_4_10"
    TOP_11_50 = "top_11_50"
    TOP_51_MORE = "top_51_more"


class BrokenRedirectReasonEnum(StrEnum):
    DROPPEDMANUAL = "droppedmanual"
    DROPPEDTOOOLD = "droppedtooold"
    DROPPED = "dropped"
    CODECHANGED = "codechanged"
    NXDOMAIN = "nxdomain"
    ROBOTSDISALLOWED = "robotsdisallowed"
    CURLERROR = "curlerror"
    INVALIDTARGET = "invalidtarget"
    NOMORECANONICAL = "nomorecanonical"
    ISNOWPARKED = "isnowparked"
    TARGETCHANGED = "targetchanged"


class CountryEnum(StrEnum):
    AD = "ad"
    AE = "ae"
    AF = "af"
    AG = "ag"
    AI = "ai"
    AL = "al"
    AM = "am"
    AO = "ao"
    AR = "ar"
    AS = "as"
    AT = "at"
    AU = "au"
    AW = "aw"
    AZ = "az"
    BA = "ba"
    BB = "bb"
    BD = "bd"
    BE = "be"
    BF = "bf"
    BG = "bg"
    BH = "bh"
    BI = "bi"
    BJ = "bj"
    BN = "bn"
    BO = "bo"
    BR = "br"
    BS = "bs"
    BT = "bt"
    BW = "bw"
    BY = "by"
    BZ = "bz"
    CA = "ca"
    CD = "cd"
    CF = "cf"
    CG = "cg"
    CH = "ch"
    CI = "ci"
    CK = "ck"
    CL = "cl"
    CM = "cm"
    CN = "cn"
    CO = "co"
    CR = "cr"
    CU = "cu"
    CV = "cv"
    CY = "cy"
    CZ = "cz"
    DE = "de"
    DJ = "dj"
    DK = "dk"
    DM = "dm"
    DO = "do"
    DZ = "dz"
    EC = "ec"
    EE = "ee"
    EG = "eg"
    ES = "es"
    ET = "et"
    FI = "fi"
    FJ = "fj"
    FM = "fm"
    FO = "fo"
    FR = "fr"
    GA = "ga"
    GB = "gb"
    GD = "gd"
    GE = "ge"
    GF = "gf"
    GG = "gg"
    GH = "gh"
    GI = "gi"
    GL = "gl"
    GM = "gm"
    GN = "gn"
    GP = "gp"
    GQ = "gq"
    GR = "gr"
    GT = "gt"
    GU = "gu"
    GY = "gy"
    HK = "hk"
    HN = "hn"
    HR = "hr"
    HT = "ht"
    HU = "hu"
    ID = "id"
    IE = "ie"
    IL = "il"
    IM = "im"
    IN = "in"
    IQ = "iq"
    IS = "is"
    IT = "it"
    JE = "je"
    JM = "jm"
    JO = "jo"
    JP = "jp"
    KE = "ke"
    KG = "kg"
    KH = "kh"
    KI = "ki"
    KN = "kn"
    KR = "kr"
    KW = "kw"
    KY = "ky"
    KZ = "kz"
    LA = "la"
    LB = "lb"
    LC = "lc"
    LI = "li"
    LK = "lk"
    LS = "ls"
    LT = "lt"
    LU = "lu"
    LV = "lv"
    LY = "ly"
    MA = "ma"
    MC = "mc"
    MD = "md"
    ME = "me"
    MG = "mg"
    MK = "mk"
    ML = "ml"
    MM = "mm"
    MN = "mn"
    MQ = "mq"
    MR = "mr"
    MS = "ms"
    MT = "mt"
    MU = "mu"
    MV = "mv"
    MW = "mw"
    MX = "mx"
    MY = "my"
    MZ = "mz"
    NA = "na"
    NC = "nc"
    NE = "ne"
    NG = "ng"
    NI = "ni"
    NL = "nl"
    NO = "no"
    NP = "np"
    NR = "nr"
    NU = "nu"
    NZ = "nz"
    OM = "om"
    PA = "pa"
    PE = "pe"
    PF = "pf"
    PG = "pg"
    PH = "ph"
    PK = "pk"
    PL = "pl"
    PN = "pn"
    PR = "pr"
    PS = "ps"
    PT = "pt"
    PY = "py"
    QA = "qa"
    RE = "re"
    RO = "ro"
    RS = "rs"
    RU = "ru"
    RW = "rw"
    SA = "sa"
    SB = "sb"
    SC = "sc"
    SE = "se"
    SG = "sg"
    SH = "sh"
    SI = "si"
    SK = "sk"
    SL = "sl"
    SM = "sm"
    SN = "sn"
    SO = "so"
    SR = "sr"
    ST = "st"
    SV = "sv"
    TD = "td"
    TG = "tg"
    TH = "th"
    TJ = "tj"
    TK = "tk"
    TL = "tl"
    TM = "tm"
    TN = "tn"
    TO = "to"
    TR = "tr"
    TT = "tt"
    TW = "tw"
    TZ = "tz"
    UA = "ua"
    UG = "ug"
    US = "us"
    UY = "uy"
    UZ = "uz"
    VC = "vc"
    VE = "ve"
    VG = "vg"
    VI = "vi"
    VN = "vn"
    VU = "vu"
    WS = "ws"
    YE = "ye"
    YT = "yt"
    ZA = "za"
    ZM = "zm"
    ZW = "zw"


class CountryEnum1(StrEnum):
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CU = "CU"
    CV = "CV"
    CW = "CW"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    OTHER = "OTHER"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    SX = "SX"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"


class DataSourceEnum(StrEnum):
    GOOGLE_AI_OVERVIEWS = "google_ai_overviews"
    GOOGLE_AI_MODE = "google_ai_mode"
    CHATGPT = "chatgpt"
    GEMINI = "gemini"
    PERPLEXITY = "perplexity"
    COPILOT = "copilot"


class DeviceEnum(StrEnum):
    DESKTOP = "desktop"
    MOBILE = "mobile"


class DiscoveredStatusEnum(StrEnum):
    PAGEFOUND = "pagefound"
    LINKFOUND = "linkfound"
    LINKRESTORED = "linkrestored"


class DropReasonEnum(StrEnum):
    MANUAL = "manual"
    NORATINGUNUSED = "noratingunused"
    NOTOP = "notop"
    TOOOLD = "tooold"
    OLDUNAVAILABLE = "oldunavailable"
    RESCURSIVE = "rescursive"
    DUPLICATE = "duplicate"
    NXDOMAIN = "nxdomain"
    MALFORMED = "malformed"
    BLOCKEDPORT = "blockedport"
    DISALLOWED = "disallowed"
    UNLINKED = "unlinked"


class FilterModeEnum(StrEnum):
    ADDED = "added"
    NEW = "new"
    REMOVED = "removed"
    MISSING = "missing"
    NO_CHANGE = "no_change"


class GroupModeEnum(StrEnum):
    DOMAINS = "domains"
    PAGES = "pages"


class HistoryGroupingEnum(StrEnum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class LinkTypeEnum(StrEnum):
    REDIRECT = "redirect"
    FRAME = "frame"
    TEXT = "text"
    FORM = "form"
    CANONICAL = "canonical"
    ALTERNATE = "alternate"
    RSS = "rss"
    IMAGE = "image"


class LostReasonEnum(StrEnum):
    REMOVEDFROMHTML = "removedfromhtml"
    NOTCANONICAL = "notcanonical"
    NOINDEX = "noindex"
    PAGEREDIRECTED = "pageredirected"
    PAGEERROR = "pageerror"
    LOSTREDIRECT = "lostredirect"
    NOTFOUND = "notfound"


class MatchModeEnum(StrEnum):
    TERMS = "terms"
    PHRASE = "phrase"


class ModeEnum(StrEnum):
    EXACT = "exact"
    PREFIX = "prefix"
    DOMAIN = "domain"
    SUBDOMAINS = "subdomains"


class OrderByEnum(StrEnum):
    RELEVANCE = "relevance"
    VOLUME = "volume"


class OutputEnum(StrEnum):
    JSON = "json"
    CSV = "csv"
    XML = "xml"
    PHP = "php"


class OutputJsonPhpEnum(StrEnum):
    JSON = "json"
    PHP = "php"


class ProtocolEnum(StrEnum):
    BOTH = "both"
    HTTP = "http"
    HTTPS = "https"


class SearchEngineEnum(StrEnum):
    GOOGLE = "google"


class SerpFeaturesItemEnum(StrEnum):
    AI_OVERVIEW_SITELINK = "ai_overview_sitelink"
    SNIPPET = "snippet"
    AI_OVERVIEW = "ai_overview"
    LOCAL_PACK = "local_pack"
    SITELINK = "sitelink"
    NEWS = "news"
    IMAGE = "image"
    VIDEO = "video"
    DISCUSSION = "discussion"
    TWEET = "tweet"
    PAID_TOP = "paid_top"
    PAID_BOTTOM = "paid_bottom"
    PAID_SITELINK = "paid_sitelink"
    SHOPPING = "shopping"
    KNOWLEDGE_CARD = "knowledge_card"
    KNOWLEDGE_PANEL = "knowledge_panel"
    QUESTION = "question"
    IMAGE_TH = "image_th"
    VIDEO_TH = "video_th"
    ORGANIC_SHOPPING = "organic_shopping"


class SerpFeaturesItemEnum1(StrEnum):
    PAID_TOP = "paid_top"
    PAID_BOTTOM = "paid_bottom"
    PAID_RIGHT = "paid_right"
    PAID_SITELINK = "paid_sitelink"
    ORGANIC = "organic"
    SITELINK = "sitelink"
    SNIPPET = "snippet"
    IMAGE = "image"
    ARTICLE = "article"
    KNOWLEDGE_CARD = "knowledge_card"
    KNOWLEDGE_PANEL = "knowledge_panel"
    LOCAL_PACK = "local_pack"
    LOCAL_TEASER = "local_teaser"
    NEWS = "news"
    QUESTION = "question"
    REVIEW = "review"
    SHOPPING = "shopping"
    TWEET = "tweet"
    SPELLING = "spelling"
    VIDEO = "video"
    DISCUSSION = "discussion"
    AI_OVERVIEW = "ai_overview"
    AI_OVERVIEW_SITELINK = "ai_overview_sitelink"
    ORGANIC_SHOPPING = "organic_shopping"
    IMAGE_TH = "image_th"
    VIDEO_TH = "video_th"
    AI_OVERVIEW_FOUND = "ai_overview_found"


class StatusEnum(StrEnum):
    LEFT = "left"
    RIGHT = "right"
    BOTH = "both"


class TargetPositionEnum(StrEnum):
    IN_TOP10 = "in_top10"
    IN_TOP100 = "in_top100"


class TermsEnum(StrEnum):
    ALL = "all"
    QUESTIONS = "questions"


class TermsEnum1(StrEnum):
    ALSO_RANK_FOR = "also_rank_for"
    ALSO_TALK_ABOUT = "also_talk_about"
    ALL = "all"


class TldClassSourceEnum(StrEnum):
    GOV = "gov"
    EDU = "edu"
    NORMAL = "normal"


class ViewForEnum(StrEnum):
    TOP_10 = "top_10"
    TOP_100 = "top_100"


class VolumeModeEnum(StrEnum):
    MONTHLY = "monthly"
    AVERAGE = "average"


# ============== Batch Analysis API ==============

# Models for batch-analysis/batch-analysis
class BatchAnalysisTarget(BaseModel):
    """Request model for BatchAnalysisTarget."""

    url: str = Field(..., description="The URL of the analyzed target.")
    mode: ModeEnum = Field(..., description="The target mode used for the analysis.")
    protocol: ProtocolEnum = Field(..., description="The protocol of the target.")


class BatchAnalysisRequest(BaseModel):
    """Request model for BatchAnalysisRequest."""

    select: list[str] = Field(..., description="A list of columns to return. See response schema for valid column identifiers.")
    order_by: str | None = Field(default=None, description="The order_by parameter")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")
    targets: list[BatchAnalysisTarget] = Field(..., description="A list of targets to do batch analysis.")


class BatchAnalysisData(BaseModel):
    """Individual data item for /batch-analysis endpoint"""

    ahrefs_rank: int | None = Field(default=None, description="The strength of your target's backlink profile compared to the other websites in our database, with rank #1 being the strongest.")
    backlinks: int | None = Field(default=None, description="The total number of links from other websites pointing to your target.")
    backlinks_dofollow: int | None = Field(default=None, description="Links to your target that do not contain a “nofollow”, “ugc”, or “sponsored” value in their “rel” attribute. These links are also called “dofollow”.")
    backlinks_internal: int | None = Field(default=None, description="The total number of internal links pointing to the target's pages.")
    backlinks_nofollow: int | None = Field(default=None, description="Links to your target that contain a “nofollow”, “ugc”, or “sponsored” value in their “rel” attribute.")
    backlinks_redirect: int | None = Field(default=None, description="Links pointing to your target via a redirect.")
    domain_rating: float | None = Field(default=None, description="The strength of your target's backlink profile compared to the other websites in our database on a 100-point logarithmic scale.")
    index: int | None = Field(default=None, description="Target index number.")
    ip: str | None = Field(default=None, description="The IP address of the target.")
    linked_domains: int | None = Field(default=None, description="The number of unique domains linked from your target.")
    linked_domains_dofollow: int | None = Field(default=None, description="The number of unique domains linked from your target with followed links.")
    mode: str | None = Field(default=None, description="The target mode used for the analysis. Depending on the selected mode (Exact URL, Path, Domain, Subdomains), different parts of the website will be analyzed.")
    org_cost: int | None = Field(default=None, description="(10 units) The estimated value of your target’s monthly organic search traffic.")
    org_keywords: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 100 organic search results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword.")
    org_keywords_11_20: int | None = Field(default=None, description="The total number of unique keywords for which your target's top organic ranking position is within the 11th to 20th results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword.")
    org_keywords_1_3: int | None = Field(default=None, description="The total number of unique keywords for which your target's top organic ranking position is within the top 3 results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword.")
    org_keywords_21_50: int | None = Field(default=None, description="The total number of unique keywords for which your target's top organic ranking position is within the 21st to 50th results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword.")
    org_keywords_4_10: int | None = Field(default=None, description="The total number of unique keywords for which your target's top organic ranking position is within the 4th to 10th results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword.")
    org_keywords_51_plus: int | None = Field(default=None, description="The total number of unique keywords for which your target's top organic ranking position is the 51st result or higher. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword.")
    org_traffic: int | None = Field(default=None, description="(10 units) The estimated number of monthly visits that your target gets from organic search.")
    org_traffic_top_by_country: list[list[Any] | None] | None = Field(default=None, description="(10 units) Top countries by traffic with corresponding traffic values. (Currently only a single element is being returned with the country with the most traffic.)")
    outgoing_links: int | None = Field(default=None, description="The total number of links from your target to other domains.")
    outgoing_links_dofollow: int | None = Field(default=None, description="The total number of followed links from your target to other domains.")
    paid_ads: int | None = Field(default=None, description="The total number of unique ads of a target website or URL in paid search results.")
    paid_cost: int | None = Field(default=None, description="(10 units) The estimated cost of your target’s monthly paid search traffic.")
    paid_keywords: int | None = Field(default=None, description="The total number of keywords that your target ranks for in paid search results. When ranking for the same keyword across different locations in “All locations” mode, it's still counted as one keyword.")
    paid_traffic: int | None = Field(default=None, description="(10 units) The estimated number of monthly visits that your target gets from paid search.")
    protocol: str | None = Field(default=None, description="The protocol of the target. Possible values: `both`, `http`, `https`.")
    refdomains: int | None = Field(default=None, description="(5 units) The total number of unique domains linking to your target.")
    refdomains_dofollow: int | None = Field(default=None, description="(5 units) The number of unique domains with links to your target that do not contain a “nofollow”, “ugc”, or “sponsored” value in their “rel” attribute. These links are also called “dofollow”.")
    refdomains_nofollow: int | None = Field(default=None, description="(5 units) The number of unique domains that only have links to your target containing a “nofollow”, “ugc”, or “sponsored” value in their “rel” attribute.")
    refips: int | None = Field(default=None, description="The number of unique IP addresses with at least one domain pointing to your target. Several domains can share one IP address.")
    refips_subnets: int | None = Field(default=None, description="The number of c-class IP networks (AAA.BBB.CCC.DDD) with at least one link to your target. Example: 151.80.39.61 is the website IP address where 151.80.39.XXX is the subnet.")
    url: str | None = Field(default=None, description="The URL of the analyzed target.")
    url_rating: float | None = Field(default=None, description="URL Rating (UR) shows the strength of your target page's backlink profile on a 100-point logarithmic scale. If you analyze a domain, the homepage's UR is shown.")


class BatchAnalysisResponse(BaseModel):
    """Response model for /batch-analysis endpoint"""

    targets: list[BatchAnalysisData] | None = Field(default=None, description="The targets field")

    @property
    def data(self) -> list[BatchAnalysisData]:
        """Unwrap the response payload."""
        return self.targets or []


# ============== Brand Radar API ==============

# Models for brand-radar/ai-responses
class BrandRadarAiResponsesRequest(BaseModel):
    """Request model for BrandRadarAiResponsesRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    date: DateStr | None = Field(default=None, description="The date to search for in YYYY-MM-DD format.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    order_by: OrderByEnum = Field(default=OrderByEnum.RELEVANCE, description="The order by field.")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the niche markets of your brands.")
    competitors: str = Field(default="[]", description="A comma-separated list of competitors of your brands.")
    brand: str = Field(default="[]", description="A comma-separated list of brands to search for. At least one of brand, competitors, market or where should not be empty.")


class BrandRadarAiResponsesData(BaseModel):
    """Individual data item for /ai-responses endpoint"""

    country: str | None = Field(default=None, description="The country of the question.")
    links: list[dict[str, Any] | None] | None = Field(default=None, description="(10 units) The links used for the response.")
    question: str | None = Field(default=None, description="The question asked by the user.")
    response: str | None = Field(default=None, description="(10 units) The response from the model.")
    volume: int | None = Field(default=None, description="(10 units) Estimated monthly searches. This is based on our estimates for Google, combining the search volumes of related keywords where this question appears in People Also Ask section.")


class BrandRadarAiResponsesResponse(BaseModel):
    """Response model for /ai-responses endpoint"""

    ai_responses: list[BrandRadarAiResponsesData] | None = Field(default=None, description="The ai_responses field")

    @property
    def data(self) -> list[BrandRadarAiResponsesData]:
        """Unwrap the response payload."""
        return self.ai_responses or []


# Models for brand-radar/impressions-history
class BrandRadarImpressionsHistoryRequest(BaseModel):
    """Request model for BrandRadarImpressionsHistoryRequest."""

    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    date_to: DateStr | None = Field(default=None, description="The end date of the historical period in YYYY-MM-DD format.")
    date_from: DateStr = Field(..., description="The start date of the historical period in YYYY-MM-DD format.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the niche markets of your brand.")
    brand: str = Field(..., description="The brand to search for.")


class BrandRadarImpressionsHistoryData(BaseModel):
    """Individual data item for /impressions-history endpoint"""

    date: str | None = Field(default=None, description="date")
    impressions: int | None = Field(default=None, description="impressions")


class BrandRadarImpressionsHistoryResponse(BaseModel):
    """Response model for /impressions-history endpoint"""

    metrics: list[BrandRadarImpressionsHistoryData] | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> list[BrandRadarImpressionsHistoryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for brand-radar/impressions-overview
class BrandRadarImpressionsOverviewRequest(BaseModel):
    """Request model for BrandRadarImpressionsOverviewRequest."""

    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the niche markets of your brands.")
    competitors: str = Field(default="[]", description="A comma-separated list of competitors of your brands.")
    brand: str = Field(default="[]", description="A comma-separated list of brands to search for. At least one of brand or competitors should not be empty.")


class BrandRadarImpressionsOverviewData(BaseModel):
    """Individual data item for /impressions-overview endpoint"""

    brand: str | None = Field(default=None, description="Brand name (either your brand or a competitor provided in the request).")
    no_tracked_brands: int | None = Field(default=None, description="Estimated impressions from responses related to the specified market that do not mention any provided brands (value is zero when `market` is not specified).")
    only_competitors_brands: int | None = Field(default=None, description="Estimated impressions from responses mentioning only competitor brands.")
    only_target_brand: int | None = Field(default=None, description="Estimated impressions from responses mentioning only your brand.")
    target_and_competitors_brands: int | None = Field(default=None, description="Estimated impressions from responses mentioning both your and competitor brands.")
    total: int | None = Field(default=None, description="Total estimated impressions for your brand (includes both `only_target_brand` and `target_and_competitors_brands`).")


class BrandRadarImpressionsOverviewResponse(BaseModel):
    """Response model for /impressions-overview endpoint"""

    metrics: list[BrandRadarImpressionsOverviewData] | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> list[BrandRadarImpressionsOverviewData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for brand-radar/mentions-history
class BrandRadarMentionsHistoryRequest(BaseModel):
    """Request model for BrandRadarMentionsHistoryRequest."""

    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    date_to: DateStr | None = Field(default=None, description="The end date of the historical period in YYYY-MM-DD format.")
    date_from: DateStr = Field(..., description="The start date of the historical period in YYYY-MM-DD format.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the niche markets of your brand.")
    brand: str = Field(..., description="The brand to search for.")


class BrandRadarMentionsHistoryData(BaseModel):
    """Individual data item for /mentions-history endpoint"""

    date: str | None = Field(default=None, description="date")
    mentions: int | None = Field(default=None, description="mentions")


class BrandRadarMentionsHistoryResponse(BaseModel):
    """Response model for /mentions-history endpoint"""

    metrics: list[BrandRadarMentionsHistoryData] | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> list[BrandRadarMentionsHistoryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for brand-radar/mentions-overview
class BrandRadarMentionsOverviewRequest(BaseModel):
    """Request model for BrandRadarMentionsOverviewRequest."""

    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the niche markets of your brands.")
    competitors: str = Field(default="[]", description="A comma-separated list of competitors of your brands.")
    brand: str = Field(default="[]", description="A comma-separated list of brands to search for. At least one of brand or competitors should not be empty.")


class BrandRadarMentionsOverviewData(BaseModel):
    """Individual data item for /mentions-overview endpoint"""

    brand: str | None = Field(default=None, description="Brand name (either your brand or a competitor provided in the request).")
    no_tracked_brands: int | None = Field(default=None, description="Estimated mentions from responses related to the specified market that do not mention any provided brands (value is zero when `market` is not specified).")
    only_competitors_brands: int | None = Field(default=None, description="Estimated mentions from responses mentioning only competitor brands.")
    only_target_brand: int | None = Field(default=None, description="Estimated mentions from responses mentioning only your brand.")
    target_and_competitors_brands: int | None = Field(default=None, description="Estimated mentions from responses mentioning both your and competitor brands.")
    total: int | None = Field(default=None, description="Total estimated mentions for your brand (includes both `only_target_brand` and `target_and_competitors_brands`).")


class BrandRadarMentionsOverviewResponse(BaseModel):
    """Response model for /mentions-overview endpoint"""

    metrics: list[BrandRadarMentionsOverviewData] | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> list[BrandRadarMentionsOverviewData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for brand-radar/sov-overview
class BrandRadarSovOverviewRequest(BaseModel):
    """Request model for BrandRadarSovOverviewRequest."""

    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    data_source: DataSourceEnum = Field(..., description="The chatbot model to use.")
    market: str = Field(default="[]", description="A comma-separated list of the niche markets of your brands.")
    competitors: str = Field(default="[]", description="A comma-separated list of competitors of your brands.")
    brand: str = Field(default="[]", description="A comma-separated list of brands to search for. At least one of brand or competitors should not be empty.")


class BrandRadarSovOverviewData(BaseModel):
    """Individual data item for /sov-overview endpoint"""

    brand: str | None = Field(default=None, description="Brand name (either your brand or a competitor provided in the request).")
    share_of_voice: float | None = Field(default=None, description="Estimated share of voice for your brand.")


class BrandRadarSovOverviewResponse(BaseModel):
    """Response model for /sov-overview endpoint"""

    metrics: list[BrandRadarSovOverviewData] | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> list[BrandRadarSovOverviewData]:
        """Unwrap the response payload."""
        return self.metrics or []


# ============== Keywords Explorer API ==============

# Models for keywords-explorer/matching-terms
class KeywordsExplorerMatchingTermsRequest(BaseModel):
    """Request model for KeywordsExplorerMatchingTermsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3166-1 alpha-2).")
    search_engine: SearchEngineEnum = Field(default=SearchEngineEnum.GOOGLE, description="[Deprecated on 5 Aug 2024].")
    keywords: str | None = Field(default=None, description="A comma-separated list of keywords to show metrics for.")
    keyword_list_id: int | None = Field(default=None, description="The id of an existing keyword list to show metrics for.")
    match_mode: MatchModeEnum = Field(default=MatchModeEnum.TERMS, description="Keyword ideas contain the words from your query in any order (terms mode) or in the exact order they are written (phrase mode).")
    terms: TermsEnum = Field(default=TermsEnum.ALL, description="All keywords ideas or keywords ideas phrased as questions.")


class KeywordsExplorerMatchingTermsData(BaseModel):
    """Individual data item for /matching-terms endpoint"""

    cpc: int | None = Field(default=None, description="Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.")
    cps: float | None = Field(default=None, description="Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.")
    difficulty: int | None = Field(default=None, description="(10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.")
    first_seen: str | None = Field(default=None, description="The date when we first checked search engine results for a keyword.")
    global_volume: int | None = Field(default=None, description="(10 units) How many times per month, on average, people search for the target keyword across all countries in our database.")
    intents: dict[str, Any] | None = Field(default=None, description="(10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.")
    keyword: str | None = Field(default=None)
    parent_topic: str | None = Field(default=None, description="Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.")
    serp_features: list[SerpFeaturesItemEnum | None] | None = Field(default=None, description="The enriched results on a search engine results page (SERP) that are not traditional organic results.")
    serp_last_update: str | None = Field(default=None, description="The date when we last checked search engine results for a keyword.")
    traffic_potential: int | None = Field(default=None, description="(10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.")
    volume: int | None = Field(default=None, description="(10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.")
    volume_desktop_pct: float | None = Field(default=None, description="The percentage of searches for a keyword performed on desktop devices.")
    volume_mobile_pct: float | None = Field(default=None, description="The percentage of searches for a keyword performed on mobile devices.")
    volume_monthly: int | None = Field(default=None, description="(10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter")


class KeywordsExplorerMatchingTermsResponse(BaseModel):
    """Response model for /matching-terms endpoint"""

    keywords: list[KeywordsExplorerMatchingTermsData] | None = Field(default=None, description="The keywords field")

    @property
    def data(self) -> list[KeywordsExplorerMatchingTermsData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for keywords-explorer/overview
class KeywordsExplorerOverviewRequest(BaseModel):
    """Request model for KeywordsExplorerOverviewRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    volume_monthly_date_to: DateStr | None = Field(default=None, description="The end date in YYYY-MM-DD format for retrieving historical monthly search volumes in the `volume_monthly_history` field. Required only if `volume_monthly_history` is requested.")
    volume_monthly_date_from: DateStr | None = Field(default=None, description="The start date in YYYY-MM-DD format for retrieving historical monthly search volumes in the `volume_monthly_history` field. Required only if `volume_monthly_history` is requested.")
    target_mode: ModeEnum | None = Field(default=None, description="The scope of the target URL you specified.")
    target: str | None = Field(default=None, description="The target of the search: a domain or a URL.")
    target_position: TargetPositionEnum | None = Field(default=None, description="Filters keywords based on the ranking position of the specified `target`.")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3166-1 alpha-2).")
    search_engine: SearchEngineEnum = Field(default=SearchEngineEnum.GOOGLE, description="[Deprecated on 5 Aug 2024].")
    keywords: str | None = Field(default=None, description="A comma-separated list of keywords to show metrics for.")
    keyword_list_id: int | None = Field(default=None, description="The id of an existing keyword list to show metrics for.")


class KeywordsExplorerOverviewData(BaseModel):
    """Individual data item for /overview endpoint"""

    clicks: int | None = Field(default=None, description="The average monthly number of clicks on the search results that people make while searching for the target keyword.")
    cpc: int | None = Field(default=None, description="Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.")
    cps: float | None = Field(default=None, description="Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.")
    difficulty: int | None = Field(default=None, description="(10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.")
    first_seen: str | None = Field(default=None, description="The date when we first checked search engine results for a keyword.")
    global_volume: int | None = Field(default=None, description="(10 units) How many times per month, on average, people search for the target keyword across all countries in our database.")
    intents: dict[str, Any] | None = Field(default=None, description="(10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.")
    keyword: str | None = Field(default=None)
    parent_topic: str | None = Field(default=None, description="Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.")
    parent_volume: int | None = Field(default=None, description="(10 units) The search volume of the parent topic.")
    searches_pct_clicks_organic_and_paid: float | None = Field(default=None, description="The average monthly percentage of people who clicked on both organic and paid results while searching for the target keyword.")
    searches_pct_clicks_organic_only: float | None = Field(default=None, description="The average monthly percentage of people who clicked only on organic results while searching for the target keyword.")
    searches_pct_clicks_paid_only: float | None = Field(default=None, description="The average monthly percentage of people who clicked only on paid results while searching for the target keyword.")
    serp_features: list[SerpFeaturesItemEnum | None] | None = Field(default=None, description="The enriched results on a search engine results page (SERP) that are not traditional organic results.")
    serp_last_update: str | None = Field(default=None, description="The date when we last checked search engine results for a keyword.")
    traffic_potential: int | None = Field(default=None, description="(10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.")
    volume: int | None = Field(default=None, description="(10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.")
    volume_desktop_pct: float | None = Field(default=None, description="The percentage of searches for a keyword performed on desktop devices.")
    volume_mobile_pct: float | None = Field(default=None, description="The percentage of searches for a keyword performed on mobile devices.")
    volume_monthly: int | None = Field(default=None, description="(10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter")
    volume_monthly_history: list[dict[str, Any] | None] | None = Field(default=None, description="(2 units per historical month, with a minimum of 50 units) Historical monthly search volume estimates of a keyword for the period set by the `volume_monthly_date_from` and `volume_monthly_date_to` parameters.")


class KeywordsExplorerOverviewResponse(BaseModel):
    """Response model for /overview endpoint"""

    keywords: list[KeywordsExplorerOverviewData] | None = Field(default=None, description="The keywords field")

    @property
    def data(self) -> list[KeywordsExplorerOverviewData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for keywords-explorer/related-terms
class KeywordsExplorerRelatedTermsRequest(BaseModel):
    """Request model for KeywordsExplorerRelatedTermsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3166-1 alpha-2).")
    keywords: str | None = Field(default=None, description="A comma-separated list of keywords to show metrics for.")
    keyword_list_id: int | None = Field(default=None, description="The id of an existing keyword list to show metrics for.")
    view_for: ViewForEnum = Field(default=ViewForEnum.TOP_10, description="View keywords for the top 10 or top 100 ranking pages.")
    terms: TermsEnum1 = Field(default=TermsEnum1.ALL, description="Related keywords which top-ranking pages also rank for (`also_rank_for`), additional keywords frequently mentioned in top-ranking pages (`also_talk_about`), or combination of both (`all`).")


class KeywordsExplorerRelatedTermsData(BaseModel):
    """Individual data item for /related-terms endpoint"""

    cpc: int | None = Field(default=None, description="Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.")
    cps: float | None = Field(default=None, description="Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.")
    difficulty: int | None = Field(default=None, description="(10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.")
    first_seen: str | None = Field(default=None, description="The date when we first checked search engine results for a keyword.")
    global_volume: int | None = Field(default=None, description="(10 units) How many times per month, on average, people search for the target keyword across all countries in our database.")
    intents: dict[str, Any] | None = Field(default=None, description="(10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.")
    keyword: str | None = Field(default=None)
    parent_topic: str | None = Field(default=None, description="Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.")
    serp_features: list[SerpFeaturesItemEnum | None] | None = Field(default=None, description="The enriched results on a search engine results page (SERP) that are not traditional organic results.")
    serp_last_update: str | None = Field(default=None, description="The date when we last checked search engine results for a keyword.")
    traffic_potential: int | None = Field(default=None, description="(10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.")
    volume: int | None = Field(default=None, description="(10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.")
    volume_desktop_pct: float | None = Field(default=None, description="The percentage of searches for a keyword performed on desktop devices.")
    volume_mobile_pct: float | None = Field(default=None, description="The percentage of searches for a keyword performed on mobile devices.")
    volume_monthly: int | None = Field(default=None, description="(10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter")


class KeywordsExplorerRelatedTermsResponse(BaseModel):
    """Response model for /related-terms endpoint"""

    keywords: list[KeywordsExplorerRelatedTermsData] | None = Field(default=None, description="The keywords field")

    @property
    def data(self) -> list[KeywordsExplorerRelatedTermsData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for keywords-explorer/search-suggestions
class KeywordsExplorerSearchSuggestionsRequest(BaseModel):
    """Request model for KeywordsExplorerSearchSuggestionsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See the response schema for valid column identifiers, except for `volume_monthly`, which is not supported in `order_by` for this endpoint.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3166-1 alpha-2).")
    search_engine: SearchEngineEnum = Field(default=SearchEngineEnum.GOOGLE, description="[Deprecated on 5 Aug 2024].")
    keywords: str | None = Field(default=None, description="A comma-separated list of keywords to show metrics for.")
    keyword_list_id: int | None = Field(default=None, description="The id of an existing keyword list to show metrics for.")


class KeywordsExplorerSearchSuggestionsData(BaseModel):
    """Individual data item for /search-suggestions endpoint"""

    cpc: int | None = Field(default=None, description="Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.")
    cps: float | None = Field(default=None, description="Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.")
    difficulty: int | None = Field(default=None, description="(10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.")
    first_seen: str | None = Field(default=None, description="The date when we first checked search engine results for a keyword.")
    global_volume: int | None = Field(default=None, description="(10 units) How many times per month, on average, people search for the target keyword across all countries in our database.")
    intents: dict[str, Any] | None = Field(default=None, description="(10 units) Indicates the purpose behind the user's search query. Object fields: `informational`, `navigational`, `commercial`, `transactional`, `branded` or `local`. All the fields are of type `bool`, with posible values `true` or `false`.")
    keyword: str | None = Field(default=None)
    parent_topic: str | None = Field(default=None, description="Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.")
    serp_features: list[SerpFeaturesItemEnum | None] | None = Field(default=None, description="The enriched results on a search engine results page (SERP) that are not traditional organic results.")
    serp_last_update: str | None = Field(default=None, description="The date when we last checked search engine results for a keyword.")
    traffic_potential: int | None = Field(default=None, description="(10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.")
    volume: int | None = Field(default=None, description="(10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.")
    volume_desktop_pct: float | None = Field(default=None, description="The percentage of searches for a keyword performed on desktop devices.")
    volume_mobile_pct: float | None = Field(default=None, description="The percentage of searches for a keyword performed on mobile devices.")
    volume_monthly: int | None = Field(default=None, description="(10 units) An estimation of the number of searches for a keyword over the latest month. This field may not be included in the `order_by` parameter")


class KeywordsExplorerSearchSuggestionsResponse(BaseModel):
    """Response model for /search-suggestions endpoint"""

    keywords: list[KeywordsExplorerSearchSuggestionsData] | None = Field(default=None, description="The keywords field")

    @property
    def data(self) -> list[KeywordsExplorerSearchSuggestionsData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for keywords-explorer/volume-by-country
class KeywordsExplorerVolumeByCountryRequest(BaseModel):
    """Request model for KeywordsExplorerVolumeByCountryRequest."""

    limit: int | None = Field(default=None, description="The number of results to return.")
    search_engine: SearchEngineEnum = Field(default=SearchEngineEnum.GOOGLE, description="[Deprecated on 5 Aug 2024].")
    keyword: str = Field(..., description="The keyword to show metrics for.")


class KeywordsExplorerVolumeByCountryData(BaseModel):
    """Individual data item for /volume-by-country endpoint"""

    country: str | None = Field(default=None, description="The country field")
    volume: int | None = Field(default=None, description="(10 units) An estimation of the average monthly number of searches for a keyword in a given country.")


class KeywordsExplorerVolumeByCountryResponse(BaseModel):
    """Response model for /volume-by-country endpoint"""

    countries: list[KeywordsExplorerVolumeByCountryData] | None = Field(default=None, description="The countries field")

    @property
    def data(self) -> list[KeywordsExplorerVolumeByCountryData]:
        """Unwrap the response payload."""
        return self.countries or []


# Models for keywords-explorer/volume-history
class KeywordsExplorerVolumeHistoryRequest(BaseModel):
    """Request model for KeywordsExplorerVolumeHistoryRequest."""

    date_to: DateStr | None = Field(default=None, description="The end date of the historical period in YYYY-MM-DD format.")
    date_from: DateStr | None = Field(default=None, description="The start date of the historical period in YYYY-MM-DD format.")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3166-1 alpha-2).")
    keyword: str = Field(..., description="The keyword to show metrics for.")


class KeywordsExplorerVolumeHistoryData(BaseModel):
    """Individual data item for /volume-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    volume: int | None = Field(default=None, description="An estimation of the number of searches for a keyword over a given month.")


class KeywordsExplorerVolumeHistoryResponse(BaseModel):
    """Response model for /volume-history endpoint"""

    metrics: list[KeywordsExplorerVolumeHistoryData] | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> list[KeywordsExplorerVolumeHistoryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# ============== Rank Tracker API ==============

# Models for rank-tracker/competitors-overview
class RankTrackerCompetitorsOverviewRequest(BaseModel):
    """Request model for RankTrackerCompetitorsOverviewRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    date_compared: DateStr | None = Field(default=None, description="A date to compare metrics with in YYYY-MM-DD format.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")
    device: DeviceEnum = Field(..., description="Choose between mobile and desktop rankings.")
    project_id: int = Field(..., description="The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")


class RankTrackerCompetitorsOverviewData(BaseModel):
    """Individual data item for /competitors-overview endpoint"""

    competitors_list: list[dict[str, Any] | None] | None = Field(default=None, description="Competitors information for a given keyword. The following fields are included: `url`, `url_prev`, `position`, `position_prev`, `best_position_kind`, `best_position_kind`, `traffic`, `traffic_prev`, `value`, `value_prev`. Fields ending in `prev` are included only in the compared view.")
    country: CountryEnum1 | None = Field(default=None, description="The country that a given keyword is being tracked in. A two-letter country code (ISO 3166-1 alpha-2).")
    keyword: str | None = Field(default=None, description="The keyword your target ranks for.")
    keyword_difficulty: int | None = Field(default=None, description="An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.")
    keyword_has_data: bool | None = Field(default=None, description="Will return `false` if the keyword is still processing and no SERP has been fetched yet.")
    keyword_is_frozen: bool | None = Field(default=None, description="Indicates whether a keyword has exceeded the tracked keywords limit on your plan. Such keywords are \"frozen\", meaning they do not have their rankings updated.")
    language: str | None = Field(default=None, description="The SERP language that a given keyword is being tracked for.")
    location: str | None = Field(default=None, description="The location (country, state/province, or city) that a given keyword is being tracked in.")
    serp_features: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None, description="The SERP features that appear in search results for a keyword.")
    serp_updated: str | None = Field(default=None, description="The date when we last checked search engine results for a keyword.")
    serp_updated_prev: str | None = Field(default=None, description="The date when we checked search engine results up to the comparison date.")
    tags: list[str | None] | None = Field(default=None, description="A list of tags assigned to a given keyword.")
    volume: int | None = Field(default=None, description="An estimation of the average monthly number of searches for a keyword over the latest month or over the latest known 12 months of data depending on the \"volume_mode\" parameter.")


class RankTrackerCompetitorsOverviewResponse(BaseModel):
    """Response model for /competitors-overview endpoint"""

    keywords: list[RankTrackerCompetitorsOverviewData] | None = Field(default=None, description="The keywords field")

    @property
    def data(self) -> list[RankTrackerCompetitorsOverviewData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for rank-tracker/competitors-pages
class RankTrackerCompetitorsPagesRequest(BaseModel):
    """Request model for RankTrackerCompetitorsPagesRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    target_and_tracked_competitors_only: bool = Field(default=False, description="Restrict pages to target and tracked competitors")
    date_compared: DateStr | None = Field(default=None, description="A date to compare metrics with in YYYY-MM-DD format.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")
    device: DeviceEnum = Field(..., description="Choose between mobile and desktop rankings.")
    project_id: int = Field(..., description="The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")


class RankTrackerCompetitorsPagesData(BaseModel):
    """Individual data item for /competitors-pages endpoint"""

    keywords: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 100 organic search results.")
    share_of_traffic_value: float | None = Field(default=None, description="The share of your target's organic search traffic value compared to the total organic search traffic value for all tracked keywords.")
    share_of_traffic_value_prev: float | None = Field(default=None, description="The share of traffic value on the comparison date.")
    share_of_voice: float | None = Field(default=None, description="The share of your target's organic search traffic compared to the total organic search traffic for all tracked keywords.")
    share_of_voice_prev: float | None = Field(default=None, description="The share of voice on the comparison date.")
    status: StatusEnum | None = Field(default=None, description="The status of a page: the new page that just started to rank (\"left\"), the lost page that disappeared from search results (\"right\"), or no change (\"both\").")
    title: str | None = Field(default=None, description="The title displayed for the page in its top keyword's SERP.")
    title_prev: str | None = Field(default=None, description="The title on the comparison date.")
    traffic: int | None = Field(default=None, description="An estimation of the number of monthly visits that a page gets from organic search.")
    traffic_prev: int | None = Field(default=None, description="The traffic on the comparison date.")
    traffic_value: int | None = Field(default=None, description="The estimated value of a page’s monthly organic search traffic, in USD cents.")
    traffic_value_prev: int | None = Field(default=None, description="The traffic value on the comparison date.")
    url: str | None = Field(default=None, description="The page URL.")


class RankTrackerCompetitorsPagesResponse(BaseModel):
    """Response model for /competitors-pages endpoint"""

    competitors_pages: list[RankTrackerCompetitorsPagesData] | None = Field(default=None, alias="competitors-pages", description="The competitors-pages field")

    @property
    def data(self) -> list[RankTrackerCompetitorsPagesData]:
        """Unwrap the response payload."""
        return self.competitors_pages or []


# Models for rank-tracker/competitors-stats
class RankTrackerCompetitorsStatsRequest(BaseModel):
    """Request model for RankTrackerCompetitorsStatsRequest."""

    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")
    device: DeviceEnum = Field(..., description="Choose between mobile and desktop rankings.")
    project_id: int = Field(..., description="The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")


class RankTrackerCompetitorsStatsData(BaseModel):
    """Individual data item for /competitors-stats endpoint"""

    ai_overview_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in an AI Overview.")
    average_position: float | None = Field(default=None, description="The average of your target's top organic positions across all tracked keywords.")
    competitor: str | None = Field(default=None, description="Competitor's URL.")
    discussions_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in Discussions and forums.")
    featured_snippet_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in a Featured snippet.")
    image_pack_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in an Image pack.")
    knowledge_card_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in a Knowledge card.")
    knowledge_panel_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in a Knowledge panel.")
    pos_11_20: int | None = Field(default=None, description="The total number of tracked keywords for which your target's top organic position is within the 11th to 20th results.")
    pos_1_3: int | None = Field(default=None, description="The total number of tracked keywords for which your target's top organic position is within the top 3 results.")
    pos_21_50: int | None = Field(default=None, description="The total number of tracked keywords for which your target's top organic position is within the 21st to 50th results.")
    pos_4_10: int | None = Field(default=None, description="The total number of tracked keywords for which your target's top organic position is within the 4th to 10th results.")
    pos_51_plus: int | None = Field(default=None, description="The total number of tracked keywords for which your target's top organic position is the 51st or higher.")
    pos_no_rank: int | None = Field(default=None, description="The total number of tracked keywords where your target doesn't rank.")
    share_of_traffic_value: float | None = Field(default=None, description="The share of your target's organic search traffic value compared to the total organic search traffic value for all tracked keywords.")
    share_of_voice: float | None = Field(default=None, description="The share of your target's organic search traffic compared to the total organic search traffic for all tracked keywords.")
    sitelinks_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in Sitelinks.")
    thumbnail_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in a Thumbnail.")
    top_stories_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in Top stories.")
    traffic: int | None = Field(default=None, description="The estimated number of monthly visits that your target gets from organic search for all tracked keywords.")
    traffic_value: int | None = Field(default=None, description="The estimated value of your target's monthly organic search traffic for all tracked keywords.")
    video_preview_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in a Video preview.")
    videos_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in Videos.")
    x_count: int | None = Field(default=None, description="The total number of tracked keywords for which your target ranks in an X (Twitter) widget.")


class RankTrackerCompetitorsStatsResponse(BaseModel):
    """Response model for /competitors-stats endpoint"""

    competitors_metrics: list[RankTrackerCompetitorsStatsData] | None = Field(default=None, alias="competitors-metrics", description="The competitors-metrics field")

    @property
    def data(self) -> list[RankTrackerCompetitorsStatsData]:
        """Unwrap the response payload."""
        return self.competitors_metrics or []


# Models for rank-tracker/overview
class RankTrackerOverviewRequest(BaseModel):
    """Request model for RankTrackerOverviewRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    date_compared: DateStr | None = Field(default=None, description="A date to compare metrics with in YYYY-MM-DD format.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")
    device: DeviceEnum = Field(..., description="Choose between mobile and desktop rankings.")
    project_id: int = Field(..., description="The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")


class RankTrackerOverviewData(BaseModel):
    """Individual data item for /overview endpoint"""

    best_position_has_thumbnail: bool | None = Field(default=None, description="The top position (or target URL’s, if set) has a thumbnail.")
    best_position_has_thumbnail_previous: bool | None = Field(default=None, description="The top position (or target URL’s, if set) has a thumbnail on the comparison date.")
    best_position_has_video_preview: bool | None = Field(default=None, description="The top position (or target URL’s, if set) has a video preview.")
    best_position_has_video_preview_previous: bool | None = Field(default=None, description="The top position (or target URL’s, if set) has a video preview on the comparison date.")
    best_position_kind: BestPositionKindEnum | None = Field(default=None, description="The kind of top position (or target URL’s, if set): organic, paid, or a SERP feature.")
    best_position_kind_previous: BestPositionKindEnum | None = Field(default=None, description="The kind of top position (or target URL’s, if set) on the comparison date.")
    clicks: int | None = Field(default=None, description="Clicks metric refers to the average monthly number of clicks on the search results that people make while searching for the target keyword. Some searches generate clicks on multiple results, while others might not end in any clicks at all.")
    clicks_per_search: float | None = Field(default=None, description="Clicks Per Search is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.")
    cost_per_click: int | None = Field(default=None, description="Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword.")
    country: CountryEnum1 | None = Field(default=None, description="The country that a given keyword is being tracked in. A two-letter country code (ISO 3166-1 alpha-2).")
    country_prev: CountryEnum1 | None = Field(default=None, description="The country that a given keyword is being tracked in on the comparison date. A two-letter country code (ISO 3166-1 alpha-2).")
    created_at: str | None = Field(default=None, description="The date when a keyword was added to the project.")
    is_branded: bool | None = Field(default=None, description="User intent: branded. The user is searching for a specific brand or company name.")
    is_commercial: bool | None = Field(default=None, description="User intent: commercial. The user is comparing products or services before making a purchase decision.")
    is_informational: bool | None = Field(default=None, description="User intent: informational. The user is looking for information or an answer to a specific question.")
    is_local: bool | None = Field(default=None, description="User intent: local. The user is looking for information relevant to a specific location or nearby services.")
    is_navigational: bool | None = Field(default=None, description="User intent: navigational. The user is searching for a specific website or web page.")
    is_transactional: bool | None = Field(default=None, description="User intent: transactional. The user is ready to complete an action, often a purchase.")
    keyword: str | None = Field(default=None, description="The keyword your target ranks for.")
    keyword_difficulty: int | None = Field(default=None, description="An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.")
    keyword_has_data: bool | None = Field(default=None, description="Will return `false` if the keyword is still processing and no SERP has been fetched yet.")
    keyword_is_frozen: bool | None = Field(default=None, description="Indicates whether a keyword has exceeded the tracked keywords limit on your plan. Such keywords are \"frozen\", meaning they do not have their rankings updated.")
    keyword_prev: str | None = Field(default=None, description="The keyword your target ranks for on the comparison date.")
    language: str | None = Field(default=None, description="The SERP language that a given keyword is being tracked for.")
    language_prev: str | None = Field(default=None, description="The SERP language on the comparison date.")
    location: str | None = Field(default=None, description="The location (country, state/province, or city) that a given keyword is being tracked in.")
    location_prev: str | None = Field(default=None, description="The location (country, state/province, or city) that a given keyword is being tracked in on the comparison date.")
    parent_topic: str | None = Field(default=None, description="Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead.  To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.")
    position: int | None = Field(default=None, description="The top position (or target URL’s, if set) in organic search.")
    position_diff: int | None = Field(default=None, description="The change in top position (or target URL’s, if set) between selected dates.")
    position_prev: int | None = Field(default=None, description="The top position (or target URL’s, if set) on the comparison date.")
    search_type_image: float | None = Field(default=None, description="Search type Image shows the percentage of searches for a keyword made for images, highlighting interest in visual content.")
    search_type_news: float | None = Field(default=None, description="Search type News shows the percentage of searches for a keyword made for news articles.")
    search_type_video: float | None = Field(default=None, description="Search type Video shows the percentage of searches for a keyword made for video, reflecting interest in video content.")
    search_type_web: float | None = Field(default=None, description="Search type Web shows the percentage of searches for a keyword made for general web content, indicating interest in a wide range of information.")
    serp_features: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None, description="The SERP features that appear in search results for a keyword.")
    serp_features_prev: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None, description="The SERP features that appear in search results for a keyword on the comparison date.")
    serp_updated: str | None = Field(default=None, description="The date when we last checked search engine results for a keyword.")
    serp_updated_prev: str | None = Field(default=None, description="The date when we checked search engine results up to the comparison date.")
    tags: list[str | None] | None = Field(default=None, description="A list of tags assigned to a given keyword.")
    tags_prev: list[str | None] | None = Field(default=None, description="A list of tags assigned to a given keyword on the comparison date.")
    target_positions_count: int | None = Field(default=None, description="The number of target URLs ranking for a keyword.")
    traffic: int | None = Field(default=None, description="An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the \"volume_mode\" parameter.")
    traffic_diff: int | None = Field(default=None, description="The change in traffic between your selected dates.")
    traffic_prev: int | None = Field(default=None, description="An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the \"volume_mode\" parameter.")
    url: str | None = Field(default=None, description="The top-ranking URL (or target URL, if set) in organic search.")
    url_prev: str | None = Field(default=None, description="The top-ranking URL (or target URL, if set) on the comparison date.")
    volume: int | None = Field(default=None, description="An estimation of the average monthly number of searches for a keyword over the latest month or over the latest known 12 months of data depending on the \"volume_mode\" parameter.")
    volume_desktop_pct: float | None = Field(default=None, description="The percentage of the total search volume that comes from desktop devices.")
    volume_mobile_pct: float | None = Field(default=None, description="The percentage of the total search volume that comes from mobile devices.")


class RankTrackerOverviewResponse(BaseModel):
    """Response model for /overview endpoint"""

    overviews: list[RankTrackerOverviewData] | None = Field(default=None, description="The overviews field")

    @property
    def data(self) -> list[RankTrackerOverviewData]:
        """Unwrap the response payload."""
        return self.overviews or []


# Models for rank-tracker/serp-overview
class RankTrackerSerpOverviewRequest(BaseModel):
    """Request model for RankTrackerSerpOverviewRequest."""

    top_positions: int | None = Field(default=None, description="The number of top organic SERP positions to return. If not specified, all available positions will be returned.")
    device: DeviceEnum = Field(..., description="Choose between mobile and desktop rankings.")
    date: str | None = Field(default=None, description="A timestamp on which the last available SERP Overview is returned in YYYY-MM-DDThh:mm:ss format. If it is not specified, the most recent SERP Overview is returned.")
    location_id: int | None = Field(default=None, description="The location ID of a tracked keyword.You can use the `management/project-keywords` endpoint to get country codes, language codes and location IDs for your tracked keywords.")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3166-1 alpha-2).")
    language_code: str | None = Field(default=None, description="The language code of a tracked keyword.You can use the `management/project-keywords` endpoint to get country codes, language codes and location IDs for your tracked keywords.")
    keyword: str = Field(..., description="The keyword to return SERP Overview for.")
    project_id: int = Field(..., description="The unique identifier of the project. You can find it in the URL of your Rank Tracker project in Ahrefs: `https://app.ahrefs.com/rank-tracker/overview/#project_id#`")


class RankTrackerSerpOverviewData(BaseModel):
    """Individual data item for /serp-overview endpoint"""

    position: int | None = Field(default=None, description="The position of the search result in SERP.")
    title: str | None = Field(default=None, description="The title of a ranking page.")
    url: str | None = Field(default=None, description="The URL of a ranking page.")
    type: list[str | None] | None = Field(default=None, description="The kind of the position: organic, paid, or a SERP feature. Allowed values: `ai_overview`, `ai_overview_sitelink`, `discussion`, `image`, `image_th`, `knowledge_card`, `knowledge_panel`, `local_pack`, `organic`, `organic_shopping`, `paid_top`, `paid_bottom`, `paid_right`, `question`, `sitelink`, `snippet`, `top_story`, `tweet`, `video`, `video_th`.")
    update_date: str | None = Field(default=None, description="The date when we checked search engine results for a keyword.")
    nr_words: int | None = Field(default=None, description="The total number of words present in the HTML of a web page.")
    domain_rating: float | None = Field(default=None, description="The strength of a domain’s backlink profile compared to the others in our database on a 100-point scale.")
    url_rating: float | None = Field(default=None, description="The strength of a page's backlink profile on a 100-point logarithmic scale.")
    ahrefs_rank: int | None = Field(default=None, description="The strength of a domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.")
    backlinks: int | None = Field(default=None, description="The total number of links from other websites pointing to a search result.")
    refdomains: int | None = Field(default=None, description="The total number of unique domains linking to a search result.")
    traffic: int | None = Field(default=None, description="An estimation of the monthly organic search traffic that a result gets from all the keywords that it ranks for.")
    value: int | None = Field(default=None, description="The estimated value of a page’s monthly organic search traffic, in USD cents.")
    keywords: int | None = Field(default=None, description="The total number of keywords that a search result ranks for in the top 100 organic positions.")
    top_keyword: str | None = Field(default=None, description="The keyword that brings the most organic traffic to a search result.")
    top_keyword_volume: int | None = Field(default=None, description="An estimation of the average monthly number of searches for the top keyword over the latest known 12 months of data.")


class RankTrackerSerpOverviewResponse(BaseModel):
    """Response model for /serp-overview endpoint"""

    positions: list[RankTrackerSerpOverviewData] | None = Field(default=None, description="The positions field")

    @property
    def data(self) -> list[RankTrackerSerpOverviewData]:
        """Unwrap the response payload."""
        return self.positions or []


# ============== Serp Overview API ==============

# Models for serp-overview/serp-overview
class SerpOverviewRequest(BaseModel):
    """Request model for SerpOverviewRequest."""

    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    top_positions: int | None = Field(default=None, description="The number of top organic SERP positions to return. If not specified, all available positions will be returned.")
    date: str | None = Field(default=None, description="A timestamp on which the last available SERP Overview is returned in YYYY-MM-DDThh:mm:ss format. If it is not specified, the most recent SERP Overview is returned.")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3166-1 alpha-2).")
    keyword: str = Field(..., description="The keyword to return SERP Overview for.")


class SerpOverviewData(BaseModel):
    """Individual data item for /serp-overview endpoint"""

    ahrefs_rank: int | None = Field(default=None, description="The strength of a domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.")
    backlinks: int | None = Field(default=None, description="The total number of links from other websites pointing to a search result.")
    domain_rating: float | None = Field(default=None, description="The strength of a domain’s backlink profile compared to the others in our database on a 100-point scale.")
    keywords: int | None = Field(default=None, description="The total number of keywords that a search result ranks for in the top 100 organic positions.")
    position: int | None = Field(default=None, description="The position of the search result in SERP.")
    refdomains: int | None = Field(default=None, description="(5 units) The total number of unique domains linking to a search result.")
    title: str | None = Field(default=None, description="The title of a ranking page.")
    top_keyword: str | None = Field(default=None, description="The keyword that brings the most organic traffic to a search result.")
    top_keyword_volume: int | None = Field(default=None, description="(10 units) An estimation of the average monthly number of searches for the top keyword over the latest known 12 months of data.")
    traffic: int | None = Field(default=None, description="(10 units) An estimation of the monthly organic search traffic that a result gets from all the keywords that it ranks for.")
    type: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None, description="The kind of the position: organic, paid, or a SERP feature.")
    update_date: str | None = Field(default=None, description="The date when we checked search engine results for a keyword.")
    url: str | None = Field(default=None, description="The URL of a ranking page.")
    url_rating: float | None = Field(default=None, description="The strength of a page's backlink profile on a 100-point logarithmic scale.")
    value: int | None = Field(default=None, description="(10 units) The estimated value of a page’s monthly organic search traffic, in USD cents.")


class SerpOverviewResponse(BaseModel):
    """Response model for /serp-overview endpoint"""

    positions: list[SerpOverviewData] | None = Field(default=None, description="The positions field")

    @property
    def data(self) -> list[SerpOverviewData]:
        """Unwrap the response payload."""
        return self.positions or []


# ============== Site Audit API ==============

# Models for site-audit/issues
class SiteAuditIssuesRequest(BaseModel):
    """Request model for SiteAuditIssuesRequest."""

    date_compared: str | None = Field(default=None, description="A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to compare metrics with. Follows the same rules as the `date` field.")
    date: str | None = Field(default=None, description="A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC.")
    project_id: int = Field(..., description="The unique identifier of the project. You can find it in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#`")


class SiteAuditIssuesData(BaseModel):
    """Individual data item for /issues endpoint"""

    issue_id: str | None = Field(default=None, description="The unique identifier of the issue.")
    name: str | None = Field(default=None, description="The name of the issue.")
    importance: str | None = Field(default=None, description="The importance of the issue. Possible values: `Error`, `Warning`, `Notice`.")
    category: str | None = Field(default=None, description="The category of the issue. Possible values: `Internal pages`, `Indexability`, `Links`, `Redirects`, `Content`, `Social tags`, `Duplicates`, `Localization`, `Usability and performance`, `Images`, `JavaScript`, `CSS`, `Sitemaps`, `External pages`, `Other`.")
    is_indexable: bool | None = Field(default=None, description="True if the issue applies only to indexable pages.")
    crawled: int | None = Field(default=None, description="Number of URLs currently affected by the issue.")
    change: int | None = Field(default=None, description="Difference in the number of affected URLs between the specified dates.")
    added: int | None = Field(default=None, description="Number of URLs that have the issue on the current date but did not have it on the previous date.")
    new: int | None = Field(default=None, description="Number of newly discovered URLs that have the issue on the current date.")
    removed: int | None = Field(default=None, description="Number of URLs that had the issue on the previous date but no longer have it on the current date.")
    missing: int | None = Field(default=None, description="Number of URLs that had the issue on the previous date but cannot be found on the current date.")


class SiteAuditIssuesResponse(BaseModel):
    """Response model for /issues endpoint"""

    issues: list[SiteAuditIssuesData] | None = Field(default=None, description="The issues field")

    @property
    def data(self) -> list[SiteAuditIssuesData]:
        """Unwrap the response payload."""
        return self.issues or []


# Models for site-audit/page-content
class SiteAuditPageContentRequest(BaseModel):
    """Request model for SiteAuditPageContentRequest."""

    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    date: str | None = Field(default=None, description="A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC.")
    target_url: str = Field(..., description="The URL of the page to retrieve content for.")
    project_id: int = Field(..., description="The unique identifier of the project. Only projects with verified ownership are supported. You can find the project ID in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#`")


class SiteAuditPageContentData(BaseModel):
    """Individual data item for /page-content endpoint"""

    crawl_datetime: str | None = Field(default=None, description="The timestamp when the page was crawled.")
    page_text: str | None = Field(default=None, description="The text extracted from the page content.")
    raw_html: str | None = Field(default=None, description="The raw HTML of the page.")
    rendered_html: str | None = Field(default=None, description="The rendered HTML of the page.")


class SiteAuditPageContentResponse(BaseModel):
    """Response model for /page-content endpoint"""

    page_content: SiteAuditPageContentData | None = Field(default=None, alias="page-content", description="The page-content field")

    @property
    def data(self) -> SiteAuditPageContentData | None:
        """Unwrap the response payload."""
        return self.page_content


# Models for site-audit/page-explorer
class SiteAuditPageExplorerRequest(BaseModel):
    """Request model for SiteAuditPageExplorerRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(default="page_rating,url,is_rendered,http_code,content_type,title,meta_description,h1,traffic,canonical,canonical_code,redirect,redirect_code,compliant,page_is_noindex,page_is_nofollow,incoming_all_links,links_count_internal,links_count_external,links_count_internal4xx,links_count_external4xx,hreflang_issues,psi_crux_cls_category,psi_crux_lcp_category,psi_crux_inp_category,jsonld_schema_types,jsonld_validation_kinds,origin,depth", description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    filter_mode: FilterModeEnum | None = Field(default=None, description="Indicates which pages to return compared to the previous crawl. If not specified, all URLs that match your filter conditions are returned. `added`: URLs that are a new match for your filter conditions. `new`: URLs that are newly crawled and match your filter conditions. `removed`: URLs that stopped matching your filter conditions. `missing`: URLs that weren't crawled, but previously matched your filter conditions. `no_change`: URLs that match your filter conditions in a crawl and the crawl before it.")
    issue_id: str | None = Field(default=None, description="The unique identifier of an issue. When specified, only URLs affected by this issue are returned. You can get issue IDs by querying the `site-audit/issues` endpoint.")
    date_compared: str | None = Field(default=None, description="A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to compare metrics with. Follows the same rules as the `date` field.")
    date: str | None = Field(default=None, description="A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC.")
    project_id: int = Field(..., description="The unique identifier of the project. Only projects with verified ownership are supported. You can find the project ID in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#`")


class SiteAuditPageExplorerData(BaseModel):
    """Individual data item for /page-explorer endpoint"""

    ai_content_level: str | None = Field(default=None, description="The estimated percentage of AI-generated text on the page. Possible values: `None`, `Low`, `Moderate`, `High`, `Very High`")
    ai_content_status: str | None = Field(default=None, description="AI detection status for each page. Possible values: - `Success`: Content analyzed successfully - `Content_too_short`: Not enough text for reliable detection - `Not_eligible`: URL isn't an internal HTML page - `Failed`: Internal issue prevented detection - `Detection_off`: Disabled in Crawl settings")
    alternate: int | None = Field(default=None, description="The number of incoming external links from rel=\"alternate\" attributes on the pages (data from Ahrefs' Site Explorer database)")
    alternate_diff: int | None = Field(default=None, description="The number of incoming external links from rel=\"alternate\" attributes on the pages (data from Ahrefs' Site Explorer database)")
    alternate_prev: int | None = Field(default=None, description="The number of incoming external links from rel=\"alternate\" attributes on the pages (data from Ahrefs' Site Explorer database)")
    backlinks: int | None = Field(default=None, description="The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    backlinks_diff: int | None = Field(default=None, description="The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    backlinks_prev: int | None = Field(default=None, description="The number of incoming external links (both dofollow and nofollow) pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    canonical: str | None = Field(default=None, description="The URL of the canonical version of the page")
    canonical_code: int | None = Field(default=None, description="The HTTP status code of the canonical URL")
    canonical_counts: int | None = Field(default=None, description="The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    canonical_counts_diff: int | None = Field(default=None, description="The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    canonical_counts_prev: int | None = Field(default=None, description="The number of incoming external links from canonical pages pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    canonical_group_hash: int | None = Field(default=None, description="The ID of the group of pages that have the same canonical URL")
    canonical_is_canonical: bool | None = Field(default=None, description="Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical")
    canonical_is_canonical_prev: bool | None = Field(default=None, description="Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical")
    canonical_no_crawl_reason: str | None = Field(default=None, description="The reason why the canonical version of the page was not crawled")
    canonical_no_crawl_reason_prev: str | None = Field(default=None, description="The reason why the canonical version of the page was not crawled")
    canonical_prev: str | None = Field(default=None, description="The URL of the canonical version of the page")
    canonical_scheme: str | None = Field(default=None, description="The protocol of the canonical URL")
    canonical_scheme_prev: str | None = Field(default=None, description="The protocol of the canonical URL")
    compliant: bool | None = Field(default=None, description="Indicates that the page is indexable. An indexable page is an HTML page returning the 200 HTTP status code that has neither the \"rel=canonical\" tag pointing to a different URL nor the \"noindex\" directive")
    compliant_prev: bool | None = Field(default=None, description="Indicates that the page is indexable. An indexable page is an HTML page returning the 200 HTTP status code that has neither the \"rel=canonical\" tag pointing to a different URL nor the \"noindex\" directive")
    compression: str | None = Field(default=None, description="The data compression scheme")
    compression_prev: str | None = Field(default=None, description="The data compression scheme")
    content_encoding: str | None = Field(default=None, description="The Content-Encoding HTTP response header field")
    content_encoding_prev: str | None = Field(default=None, description="The Content-Encoding HTTP response header field")
    content_length: int | None = Field(default=None, description="The character length of content displayed on the page")
    content_length_diff: int | None = Field(default=None, description="The character length of content displayed on the page")
    content_length_prev: int | None = Field(default=None, description="The character length of content displayed on the page")
    content_nr_word: int | None = Field(default=None, description="The word count of content displayed on the page")
    content_nr_word_diff: int | None = Field(default=None, description="The word count of content displayed on the page")
    content_nr_word_prev: int | None = Field(default=None, description="The word count of content displayed on the page")
    content_type: str | None = Field(default=None, description="The Content-Type HTTP header of the page or resource. You can find the full list of content types [here](https://www.iana.org/assignments/media-types/media-types.xhtml)")
    content_type_prev: str | None = Field(default=None, description="The Content-Type HTTP header of the page or resource. You can find the full list of content types [here](https://www.iana.org/assignments/media-types/media-types.xhtml)")
    css_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why CSS files linked from the page were not crawled")
    css_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why CSS files linked from the page were not crawled")
    curl_code: int | None = Field(default=None, description="CURLcode return code. You can find the full list of CURL codes [here](https://curl.haxx.se/libcurl/c/libcurl-errors.html)")
    depth: int | None = Field(default=None, description="The minimum number of clicks required for our crawler to reach the URL from the starting point of a crawl (seed page). Please note that redirects are also counted as a level")
    depth_diff: int | None = Field(default=None, description="The minimum number of clicks required for our crawler to reach the URL from the starting point of a crawl (seed page). Please note that redirects are also counted as a level")
    depth_prev: int | None = Field(default=None, description="The minimum number of clicks required for our crawler to reach the URL from the starting point of a crawl (seed page). Please note that redirects are also counted as a level")
    dofollow: int | None = Field(default=None, description="The number of incoming external dofollow links pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    dofollow_prev: int | None = Field(default=None, description="The number of incoming external dofollow links pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    domain: str | None = Field(default=None, description="The domain name part of the URL")
    duplicate_content: int | None = Field(default=None, description="The number of pages with matching or appreciably similar content")
    duplicate_content_canonical_hreflang: int | None = Field(default=None, description="The number of page groups with matching or appreciably similar content. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_content_canonical_hreflang_diff: int | None = Field(default=None, description="The number of page groups with matching or appreciably similar content. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_content_canonical_hreflang_prev: int | None = Field(default=None, description="The number of page groups with matching or appreciably similar content. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_content_diff: int | None = Field(default=None, description="The number of pages with matching or appreciably similar content")
    duplicate_content_prev: int | None = Field(default=None, description="The number of pages with matching or appreciably similar content")
    duplicate_description: int | None = Field(default=None, description="The number of pages that have the same meta description. If the page has more than one meta description, each will be checked for duplicates")
    duplicate_description_canonical_hreflang: int | None = Field(default=None, description="The number of page groups that have the same meta description. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_description_canonical_hreflang_diff: int | None = Field(default=None, description="The number of page groups that have the same meta description. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_description_canonical_hreflang_prev: int | None = Field(default=None, description="The number of page groups that have the same meta description. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_description_diff: int | None = Field(default=None, description="The number of pages that have the same meta description. If the page has more than one meta description, each will be checked for duplicates")
    duplicate_description_prev: int | None = Field(default=None, description="The number of pages that have the same meta description. If the page has more than one meta description, each will be checked for duplicates")
    duplicate_group_identifier: int | None = Field(default=None, description="The ID of the group of pages that are interconnected via a common canonical URL, hreflang or pagination tags")
    duplicate_h1: int | None = Field(default=None, description="The number of pages that have the same H1 subheader. If the page has more than one H1 subheader, each will be checked for duplicates")
    duplicate_h1_diff: int | None = Field(default=None, description="The number of pages that have the same H1 subheader. If the page has more than one H1 subheader, each will be checked for duplicates")
    duplicate_h1_prev: int | None = Field(default=None, description="The number of pages that have the same H1 subheader. If the page has more than one H1 subheader, each will be checked for duplicates")
    duplicate_h1canonical_hreflang: int | None = Field(default=None, description="The number of page groups sharing the same H1 subheader. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_h1canonical_hreflang_diff: int | None = Field(default=None, description="The number of page groups sharing the same H1 subheader. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_h1canonical_hreflang_prev: int | None = Field(default=None, description="The number of page groups sharing the same H1 subheader. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_title: int | None = Field(default=None, description="The number of pages that have the same title. If the page has more than one title, each will be checked for duplicates")
    duplicate_title_canonical_hreflang: int | None = Field(default=None, description="The number of page groups that have the same title. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_title_canonical_hreflang_diff: int | None = Field(default=None, description="The number of page groups that have the same title. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_title_canonical_hreflang_prev: int | None = Field(default=None, description="The number of page groups that have the same title. A group includes pages united by a common canonical URL, hreflang or pagination tags")
    duplicate_title_diff: int | None = Field(default=None, description="The number of pages that have the same title. If the page has more than one title, each will be checked for duplicates")
    duplicate_title_prev: int | None = Field(default=None, description="The number of pages that have the same title. If the page has more than one title, each will be checked for duplicates")
    edu: int | None = Field(default=None, description="The number of incoming external links from .edu domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    edu_diff: int | None = Field(default=None, description="The number of incoming external links from .edu domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    edu_prev: int | None = Field(default=None, description="The number of incoming external links from .edu domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    external_code: list[dict[str, Any] | None] | None = Field(default=None, description="The list of HTTP status codes returned by the external URLs linked from the page")
    external_link_anchor: list[dict[str, Any] | None] | None = Field(default=None, description="The list of anchor texts used in external outgoing links on the page")
    external_link_anchor_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The list of anchor texts used in external outgoing links on the page")
    external_link_domain: list[str | None] | None = Field(default=None, description="The list of external domains linked to from the page")
    external_link_domain_prev: list[str | None] | None = Field(default=None, description="The list of external domains linked to from the page")
    external_links: list[str | None] | None = Field(default=None, description="The list of external outgoing links on the page")
    external_links_is_canonical: list[dict[str, Any] | None] | None = Field(default=None, description="Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical")
    external_links_is_canonical_prev: list[dict[str, Any] | None] | None = Field(default=None, description="Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical")
    external_links_prev: list[str | None] | None = Field(default=None, description="The list of external outgoing links on the page")
    external_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why the external URLs linked from the page were not crawled")
    external_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why the external URLs linked from the page were not crawled")
    external_scheme: list[str | None] | None = Field(default=None, description="The protocols of the external outgoing links on the page")
    external_scheme_prev: list[str | None] | None = Field(default=None, description="The protocols of the external outgoing links on the page")
    final_redirect: str | None = Field(default=None, description="The destination of the final redirecting URL")
    final_redirect_code: int | None = Field(default=None, description="The HTTP status code of the destination of the final redirecting URL")
    final_redirect_no_crawl_reason: str | None = Field(default=None, description="The reason why the destination of the final redirecting URL was not crawled")
    final_redirect_no_crawl_reason_prev: str | None = Field(default=None, description="The reason why the destination of the final redirecting URL was not crawled")
    final_redirect_prev: str | None = Field(default=None, description="The destination of the final redirecting URL")
    found_in_sitemaps: list[str | None] | None = Field(default=None, description="The list of sitemaps that reference the URL")
    found_in_sitemaps_length: int | None = Field(default=None, description="The number of sitemaps that reference the URL")
    found_in_sitemaps_prev: list[str | None] | None = Field(default=None, description="The list of sitemaps that reference the URL")
    gov: int | None = Field(default=None, description="The total number of incoming external links from .gov domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    gov_diff: int | None = Field(default=None, description="The total number of incoming external links from .gov domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    gov_prev: int | None = Field(default=None, description="The total number of incoming external links from .gov domains pointing to the URL (data from Ahrefs' Site Explorer database). Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    h1: list[str | None] | None = Field(default=None, description="The page H1 subheader")
    h1_prev: list[str | None] | None = Field(default=None, description="The page H1 subheader")
    h1length: list[int | None] | None = Field(default=None, description="The character length of the page H1 subheader")
    h1length_prev: list[int | None] | None = Field(default=None, description="The character length of the page H1 subheader")
    h2: list[str | None] | None = Field(default=None, description="The page H2 subheader")
    h2_prev: list[str | None] | None = Field(default=None, description="The page H2 subheader")
    hash_content: int | None = Field(default=None, description="The page content fingerprint. Pages with matching or appreciably similar content have the same content hash")
    hash_descriptions: list[int | None] | None = Field(default=None, description="meta_descriptions.hash")
    hash_h1: list[int | None] | None = Field(default=None, description="The page H1 subheader fingerprint. Pages with matching H1 tags have the same H1 hash")
    hash_text: int | None = Field(default=None, description="The page text fingerprint. Pages with matching content have the same text hash")
    hash_titles: list[int | None] | None = Field(default=None, description="The page title fingerprint. Pages with matching title tags have the same title hash")
    hreflang: list[dict[str, Any] | None] | None = Field(default=None, description="Data from hreflang attributes")
    hreflang_code_is_valid: list[dict[str, Any] | None] | None = Field(default=None, description="Indicates that hreflang data is specified properly in the hreflang tags on the page. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)")
    hreflang_code_is_valid_prev: list[dict[str, Any] | None] | None = Field(default=None, description="Indicates that hreflang data is specified properly in the hreflang tags on the page. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)")
    hreflang_country: list[dict[str, Any] | None] | None = Field(default=None, description="The list of regions specified in the hreflang tags on the page")
    hreflang_country_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The list of regions specified in the hreflang tags on the page")
    hreflang_group_hash: int | None = Field(default=None, description="The ID of the group of pages that have the same set of hreflang attributes with the same set of URLs in them")
    hreflang_inlink_urls: list[str | None] | None = Field(default=None, description="The list of incoming URLs with hreflang attribute")
    hreflang_inlink_urls_prev: list[str | None] | None = Field(default=None, description="The list of incoming URLs with hreflang attribute")
    hreflang_issues: list[str | None] | None = Field(default=None, description="The list of hreflang-related issues a page has")
    hreflang_issues_prev: list[str | None] | None = Field(default=None, description="The list of hreflang-related issues a page has")
    hreflang_language: list[dict[str, Any] | None] | None = Field(default=None, description="The list of languages specified in the hreflang tags on the page")
    hreflang_language_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The list of languages specified in the hreflang tags on the page")
    hreflang_link: list[str | None] | None = Field(default=None, description="The list of URLs specified in the hreflang tags on the page")
    hreflang_link_is_canonical: list[dict[str, Any] | None] | None = Field(default=None, description="Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical")
    hreflang_link_is_canonical_prev: list[dict[str, Any] | None] | None = Field(default=None, description="Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical")
    hreflang_link_prev: list[str | None] | None = Field(default=None, description="The list of URLs specified in the hreflang tags on the page")
    hreflang_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why URLs specified in the hreflang tags on the page were not crawled")
    hreflang_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why URLs specified in the hreflang tags on the page were not crawled")
    hreflang_pages_urls: list[str | None] | None = Field(default=None, description="List of hreflang-linked pages URLs the page belongs to")
    hreflang_pages_urls_count: int | None = Field(default=None, description="Count of hreflang-linked pages URLs the page belongs to")
    hreflang_pages_urls_count_diff: int | None = Field(default=None, description="Count of hreflang-linked pages URLs the page belongs to")
    hreflang_pages_urls_count_prev: int | None = Field(default=None, description="Count of hreflang-linked pages URLs the page belongs to")
    hreflang_pages_urls_prev: list[str | None] | None = Field(default=None, description="List of hreflang-linked pages URLs the page belongs to")
    hreflang_prev: list[dict[str, Any] | None] | None = Field(default=None, description="Data from hreflang attributes")
    html_lang: str | None = Field(default=None, description="Data from the page's HTML lang tag")
    html_lang_code_is_valid: bool | None = Field(default=None, description="Indicates that the language (or language-region) code is specified properly in the HTML lang tag. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)")
    html_lang_code_is_valid_prev: bool | None = Field(default=None, description="Indicates that the language (or language-region) code is specified properly in the HTML lang tag. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)")
    html_lang_country: str | None = Field(default=None, description="The region code specified in the page's HTML lang tag")
    html_lang_country_prev: str | None = Field(default=None, description="The region code specified in the page's HTML lang tag")
    html_lang_language: str | None = Field(default=None, description="The language code specified in the page's HTML lang tag")
    html_lang_language_prev: str | None = Field(default=None, description="The language code specified in the page's HTML lang tag")
    html_lang_prev: str | None = Field(default=None, description="Data from the page's HTML lang tag")
    http_code: int | None = Field(default=None, description="The HTTP status code returned by the URL")
    http_header: list[str | None] | None = Field(default=None, description="The HTTP headers that the web server returns")
    http_header_prev: list[str | None] | None = Field(default=None, description="The HTTP headers that the web server returns")
    http_header_robots: list[str | None] | None = Field(default=None, description="Instructions for web crawlers specified in HTTP headers")
    http_header_robots_prev: list[str | None] | None = Field(default=None, description="Instructions for web crawlers specified in HTTP headers")
    http_headers_size: int | None = Field(default=None, description="The size of the HTTP headers that the web server returns, measured in bytes")
    http_headers_size_diff: int | None = Field(default=None, description="The size of the HTTP headers that the web server returns, measured in bytes")
    http_headers_size_prev: int | None = Field(default=None, description="The size of the HTTP headers that the web server returns, measured in bytes")
    images_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why images linked from the page were not crawled")
    images_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why images linked from the page were not crawled")
    incoming_all_links: int | None = Field(default=None, description="The number of incoming links to the URL of all types")
    incoming_all_links_diff: int | None = Field(default=None, description="The number of incoming links to the URL of all types")
    incoming_all_links_prev: int | None = Field(default=None, description="The number of incoming links to the URL of all types")
    incoming_canonical: int | None = Field(default=None, description="Shows how many times the URL is linked to from a rel=\"canonical\" element")
    incoming_canonical_diff: int | None = Field(default=None, description="Shows how many times the URL is linked to from a rel=\"canonical\" element")
    incoming_canonical_prev: int | None = Field(default=None, description="Shows how many times the URL is linked to from a rel=\"canonical\" element")
    incoming_css: int | None = Field(default=None, description="The number of incoming links to the CSS file")
    incoming_css_diff: int | None = Field(default=None, description="The number of incoming links to the CSS file")
    incoming_css_prev: int | None = Field(default=None, description="The number of incoming links to the CSS file")
    incoming_follow: int | None = Field(default=None, description="The number of incoming dofollow links to the URL from hyperlinks")
    incoming_follow_diff: int | None = Field(default=None, description="The number of incoming dofollow links to the URL from hyperlinks")
    incoming_follow_prev: int | None = Field(default=None, description="The number of incoming dofollow links to the URL from hyperlinks")
    incoming_hreflang: int | None = Field(default=None, description="Shows how many times the URL is linked to from a rel=\"alternate\" hreflang=\"x\" attribute")
    incoming_hreflang_diff: int | None = Field(default=None, description="Shows how many times the URL is linked to from a rel=\"alternate\" hreflang=\"x\" attribute")
    incoming_hreflang_prev: int | None = Field(default=None, description="Shows how many times the URL is linked to from a rel=\"alternate\" hreflang=\"x\" attribute")
    incoming_image: int | None = Field(default=None, description="The number of incoming links to the image file")
    incoming_image_diff: int | None = Field(default=None, description="The number of incoming links to the image file")
    incoming_image_prev: int | None = Field(default=None, description="The number of incoming links to the image file")
    incoming_js: int | None = Field(default=None, description="The number of incoming links to the JS file")
    incoming_js_diff: int | None = Field(default=None, description="The number of incoming links to the JS file")
    incoming_js_prev: int | None = Field(default=None, description="The number of incoming links to the JS file")
    incoming_links: int | None = Field(default=None, description="The number of incoming links to the URL from hyperlinks")
    incoming_links_diff: int | None = Field(default=None, description="The number of incoming links to the URL from hyperlinks")
    incoming_links_prev: int | None = Field(default=None, description="The number of incoming links to the URL from hyperlinks")
    incoming_nofollow: int | None = Field(default=None, description="The number of incoming nofollow links to the URL from hyperlinks")
    incoming_nofollow_diff: int | None = Field(default=None, description="The number of incoming nofollow links to the URL from hyperlinks")
    incoming_nofollow_prev: int | None = Field(default=None, description="The number of incoming nofollow links to the URL from hyperlinks")
    incoming_pagination: int | None = Field(default=None, description="Shows how many times the URL is linked to from rel=\"prev\" or rel=\"next\" elements on pages")
    incoming_pagination_diff: int | None = Field(default=None, description="Shows how many times the URL is linked to from rel=\"prev\" or rel=\"next\" elements on pages")
    incoming_pagination_prev: int | None = Field(default=None, description="Shows how many times the URL is linked to from rel=\"prev\" or rel=\"next\" elements on pages")
    incoming_redirect: int | None = Field(default=None, description="The number of incoming redirecting links to the URL")
    incoming_redirect_diff: int | None = Field(default=None, description="The number of incoming redirecting links to the URL")
    incoming_redirect_prev: int | None = Field(default=None, description="The number of incoming redirecting links to the URL")
    indexnow_error: str | None = Field(default=None, description="The error description for a failed auto-submission")
    indexnow_error_prev: str | None = Field(default=None, description="The error description for a failed auto-submission")
    indexnow_reason: str | None = Field(default=None, description="The reason the page was considered for auto-submission to IndexNow")
    indexnow_reason_prev: str | None = Field(default=None, description="The reason the page was considered for auto-submission to IndexNow")
    indexnow_status: str | None = Field(default=None, description="The status of IndexNow auto-submission. Possible values:  - **Success:** The page was successfully submitted to IndexNow. - **No changes detected:** No changes were detected on the page; submission was not required. - **Not eligible:** The URL isn't eligible for submission, e.g., it's not an indexable HTML page. - **Invalid API key:** IndexNow submission failed due to an invalid API key. - **Failed:** Submission to IndexNow failed; see details for the reason. - **Auto-submission is off:** Automatic submission is disabled in Crawl settings")
    indexnow_status_prev: str | None = Field(default=None, description="The status of IndexNow auto-submission. Possible values:  - **Success:** The page was successfully submitted to IndexNow. - **No changes detected:** No changes were detected on the page; submission was not required. - **Not eligible:** The URL isn't eligible for submission, e.g., it's not an indexable HTML page. - **Invalid API key:** IndexNow submission failed due to an invalid API key. - **Failed:** Submission to IndexNow failed; see details for the reason. - **Auto-submission is off:** Automatic submission is disabled in Crawl settings")
    indexnow_submitted_at: str | None = Field(default=None, description="The date and time when the URL was auto-submitted to IndexNow")
    indexnow_submitted_at_prev: str | None = Field(default=None, description="The date and time when the URL was auto-submitted to IndexNow")
    internal_code: list[dict[str, Any] | None] | None = Field(default=None, description="The list of HTTP status codes returned by the internal URLs linked to from the page")
    internal_inlink_urls: list[str | None] | None = Field(default=None, description="The list of URLs for incoming internal links")
    internal_inlink_urls_prev: list[str | None] | None = Field(default=None, description="The list of URLs for incoming internal links")
    internal_link_anchor: list[dict[str, Any] | None] | None = Field(default=None, description="The list of anchor texts used in internal outgoing links on the page")
    internal_link_anchor_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The list of anchor texts used in internal outgoing links on the page")
    internal_link_domain: list[str | None] | None = Field(default=None, description="The domain (or its subdomains, depending on the scope of the crawl) linked to from internal outgoing links on the page")
    internal_link_domain_prev: list[str | None] | None = Field(default=None, description="The domain (or its subdomains, depending on the scope of the crawl) linked to from internal outgoing links on the page")
    internal_links: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page")
    internal_links_is_canonical: list[dict[str, Any] | None] | None = Field(default=None, description="Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical")
    internal_links_is_canonical_prev: list[dict[str, Any] | None] | None = Field(default=None, description="Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical")
    internal_links_prev: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page")
    internal_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why the internal URLs linked to from the page were not crawled")
    internal_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why the internal URLs linked to from the page were not crawled")
    internal_scheme: list[str | None] | None = Field(default=None, description="The protocols of the internal outgoing links on the page")
    internal_scheme_prev: list[str | None] | None = Field(default=None, description="The protocols of the internal outgoing links on the page")
    is_html: bool | None = Field(default=None, description="Indicates that the content type of the web document is HTML")
    is_in_sitemap: bool | None = Field(default=None, description="Indicates that the URL is included in the website's sitemap file")
    is_in_sitemap_prev: bool | None = Field(default=None, description="Indicates that the URL is included in the website's sitemap file")
    is_page_title_used_in_serp: bool | None = Field(default=None, description="Indicates that the page and SERP titles match")
    is_redirect_loop: bool | None = Field(default=None, description="Checks if the URL has a redirect loop")
    is_redirect_loop_prev: bool | None = Field(default=None, description="Checks if the URL has a redirect loop")
    is_rendered: bool | None = Field(default=None, description="Indicates that the crawler had executed JavaScript on the page to generate content")
    is_rendered_prev: bool | None = Field(default=None, description="Indicates that the crawler had executed JavaScript on the page to generate content")
    is_valid_internal_html: bool | None = Field(default=None, description="The HTML page on the crawled domain or its subdomain that returns a 200 HTTP status code")
    is_valid_internal_html_prev: bool | None = Field(default=None, description="The HTML page on the crawled domain or its subdomain that returns a 200 HTTP status code")
    js_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why JavaScript files linked from the page were not crawled")
    js_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why JavaScript files linked from the page were not crawled")
    jsonld_attributes: list[str | None] | None = Field(default=None, description="Names of the schema properties found on the page (with indices)")
    jsonld_attributes_prev: list[str | None] | None = Field(default=None, description="Names of the schema properties found on the page (with indices)")
    jsonld_schema_types: list[str | None] | None = Field(default=None, description="Schema objects found on the page")
    jsonld_schema_types_prev: list[str | None] | None = Field(default=None, description="Schema objects found on the page")
    jsonld_validation_kinds: list[str | None] | None = Field(default=None, description="Issues with the structured data found on the page")
    jsonld_validation_kinds_prev: list[str | None] | None = Field(default=None, description="Issues with the structured data found on the page")
    jsonld_values: list[str | None] | None = Field(default=None, description="Values of the schema properties found on the page")
    jsonld_values_prev: list[str | None] | None = Field(default=None, description="Values of the schema properties found on the page")
    keywords: list[str | None] | None = Field(default=None, description="The page meta keywords")
    keywords_prev: list[str | None] | None = Field(default=None, description="The page meta keywords")
    length: int | None = Field(default=None, description="The character length of the URL")
    links_count_css: int | None = Field(default=None, description="The number of CSS files linked from the page")
    links_count_css_prev: int | None = Field(default=None, description="The number of CSS files linked from the page")
    links_count_external: int | None = Field(default=None, description="The number of external outgoing links on the page")
    links_count_external3xx: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes")
    links_count_external3xx_diff: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes")
    links_count_external3xx_prev: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes")
    links_count_external4xx: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes")
    links_count_external4xx_diff: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes")
    links_count_external4xx_prev: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes")
    links_count_external5xx: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes")
    links_count_external5xx_diff: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes")
    links_count_external5xx_prev: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes")
    links_count_external_diff: int | None = Field(default=None, description="The number of external outgoing links on the page")
    links_count_external_follow: int | None = Field(default=None, description="The number of external outgoing dofollow links on the page")
    links_count_external_follow_diff: int | None = Field(default=None, description="The number of external outgoing dofollow links on the page")
    links_count_external_follow_prev: int | None = Field(default=None, description="The number of external outgoing dofollow links on the page")
    links_count_external_nofollow: int | None = Field(default=None, description="The number of external outgoing nofollow links on the page")
    links_count_external_nofollow_diff: int | None = Field(default=None, description="The number of external outgoing nofollow links on the page")
    links_count_external_nofollow_prev: int | None = Field(default=None, description="The number of external outgoing nofollow links on the page")
    links_count_external_non_canonical: int | None = Field(default=None, description="The number of external outgoing links on the page that point to non-canonical pages")
    links_count_external_non_canonical_diff: int | None = Field(default=None, description="The number of external outgoing links on the page that point to non-canonical pages")
    links_count_external_non_canonical_prev: int | None = Field(default=None, description="The number of external outgoing links on the page that point to non-canonical pages")
    links_count_external_prev: int | None = Field(default=None, description="The number of external outgoing links on the page")
    links_count_external_xxx: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code")
    links_count_external_xxx_diff: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code")
    links_count_external_xxx_prev: int | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code")
    links_count_images: int | None = Field(default=None, description="The number of images linked from the page")
    links_count_images_diff: int | None = Field(default=None, description="The number of images linked from the page")
    links_count_images_prev: int | None = Field(default=None, description="The number of images linked from the page")
    links_count_images_with_alt: int | None = Field(default=None, description="The number of images linked from the page that have an alt attribute (alternate text)")
    links_count_images_with_alt_diff: int | None = Field(default=None, description="The number of images linked from the page that have an alt attribute (alternate text)")
    links_count_images_with_alt_prev: int | None = Field(default=None, description="The number of images linked from the page that have an alt attribute (alternate text)")
    links_count_images_without_alt: int | None = Field(default=None, description="The number of images linked from the page that have no alt attribute (alternate text)")
    links_count_images_without_alt_diff: int | None = Field(default=None, description="The number of images linked from the page that have no alt attribute (alternate text)")
    links_count_images_without_alt_prev: int | None = Field(default=None, description="The number of images linked from the page that have no alt attribute (alternate text)")
    links_count_internal: int | None = Field(default=None, description="The number of internal outgoing links on the page")
    links_count_internal3xx: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes")
    links_count_internal3xx_diff: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes")
    links_count_internal3xx_prev: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes")
    links_count_internal4xx: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes")
    links_count_internal4xx_diff: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes")
    links_count_internal4xx_prev: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes")
    links_count_internal5xx: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes")
    links_count_internal5xx_diff: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes")
    links_count_internal5xx_prev: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes")
    links_count_internal_diff: int | None = Field(default=None, description="The number of internal outgoing links on the page")
    links_count_internal_follow: int | None = Field(default=None, description="The number of internal outgoing dofollow links on the page")
    links_count_internal_follow_diff: int | None = Field(default=None, description="The number of internal outgoing dofollow links on the page")
    links_count_internal_follow_prev: int | None = Field(default=None, description="The number of internal outgoing dofollow links on the page")
    links_count_internal_nofollow: int | None = Field(default=None, description="The number of internal outgoing nofollow links on the page")
    links_count_internal_nofollow_diff: int | None = Field(default=None, description="The number of internal outgoing nofollow links on the page")
    links_count_internal_nofollow_prev: int | None = Field(default=None, description="The number of internal outgoing nofollow links on the page")
    links_count_internal_non_canonical: int | None = Field(default=None, description="The number of internal outgoing links on the page that point to non-canonical pages")
    links_count_internal_non_canonical_diff: int | None = Field(default=None, description="The number of internal outgoing links on the page that point to non-canonical pages")
    links_count_internal_non_canonical_prev: int | None = Field(default=None, description="The number of internal outgoing links on the page that point to non-canonical pages")
    links_count_internal_prev: int | None = Field(default=None, description="The number of internal outgoing links on the page")
    links_count_internal_xxx: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code")
    links_count_internal_xxx_diff: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code")
    links_count_internal_xxx_prev: int | None = Field(default=None, description="The number of internal outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code")
    links_count_js: int | None = Field(default=None, description="The number of JavaScript files linked from the page")
    links_count_js_diff: int | None = Field(default=None, description="The number of JavaScript files linked from the page")
    links_count_js_prev: int | None = Field(default=None, description="The number of JavaScript files linked from the page")
    links_css: list[str | None] | None = Field(default=None, description="The list of CSS files linked from the page")
    links_css_code: list[dict[str, Any] | None] | None = Field(default=None, description="The list of HTTP status codes returned by CSS files linked from the page")
    links_css_domain: list[str | None] | None = Field(default=None, description="The list of domains that contain CSS files linked from the page")
    links_css_domain_prev: list[str | None] | None = Field(default=None, description="The list of domains that contain CSS files linked from the page")
    links_css_prev: list[str | None] | None = Field(default=None, description="The list of CSS files linked from the page")
    links_css_scheme: list[str | None] | None = Field(default=None, description="The protocols of CSS files linked from the page")
    links_css_scheme_prev: list[str | None] | None = Field(default=None, description="The protocols of CSS files linked from the page")
    links_external3xx: list[str | None] | None = Field(default=None, description="The list of external outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes")
    links_external3xx_prev: list[str | None] | None = Field(default=None, description="The list of external outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes")
    links_external4xx: list[str | None] | None = Field(default=None, description="The list of external outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes")
    links_external4xx_prev: list[str | None] | None = Field(default=None, description="The list of external outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes")
    links_external5xx: list[str | None] | None = Field(default=None, description="The list of external outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes")
    links_external5xx_prev: list[str | None] | None = Field(default=None, description="The list of external outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes")
    links_external_follow: list[str | None] | None = Field(default=None, description="The list of external outgoing dofollow links on the page")
    links_external_follow_prev: list[str | None] | None = Field(default=None, description="The list of external outgoing dofollow links on the page")
    links_external_nofollow: list[str | None] | None = Field(default=None, description="The list of external outgoing nofollow links on the page")
    links_external_nofollow_prev: list[str | None] | None = Field(default=None, description="The list of external outgoing nofollow links on the page")
    links_external_non_canonical: list[str | None] | None = Field(default=None, description="The list of external outgoing links on the page that point to non-canonical pages")
    links_external_non_canonical_prev: list[str | None] | None = Field(default=None, description="The list of external outgoing links on the page that point to non-canonical pages")
    links_external_xxx: list[str | None] | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code")
    links_external_xxx_prev: list[str | None] | None = Field(default=None, description="The number of external outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code")
    links_hreflang_code: list[dict[str, Any] | None] | None = Field(default=None, description="The list of HTTP status codes returned by the URLs specified in hreflang tags on the page")
    links_images: list[str | None] | None = Field(default=None, description="The list of images linked from the page")
    links_images_alt: list[dict[str, Any] | None] | None = Field(default=None, description="The list of alternate texts of images linked from the page")
    links_images_alt_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The list of alternate texts of images linked from the page")
    links_images_code: list[dict[str, Any] | None] | None = Field(default=None, description="The list of HTTP status codes returned by images linked from the page")
    links_images_domain: list[str | None] | None = Field(default=None, description="The list of domains that contain images linked from the page")
    links_images_domain_prev: list[str | None] | None = Field(default=None, description="The list of domains that contain images linked from the page")
    links_images_prev: list[str | None] | None = Field(default=None, description="The list of images linked from the page")
    links_images_scheme: list[str | None] | None = Field(default=None, description="The protocols of images linked from the page")
    links_images_scheme_prev: list[str | None] | None = Field(default=None, description="The protocols of images linked from the page")
    links_images_with_alt: list[str | None] | None = Field(default=None, description="The list of images linked from the page that have an alt attribute (alternate text)")
    links_images_with_alt_prev: list[str | None] | None = Field(default=None, description="The list of images linked from the page that have an alt attribute (alternate text)")
    links_images_without_alt: list[str | None] | None = Field(default=None, description="The list of images linked from the page that have no alt attribute (alternate text)")
    links_images_without_alt_prev: list[str | None] | None = Field(default=None, description="The list of images linked from the page that have no alt attribute (alternate text)")
    links_internal3xx: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes")
    links_internal3xx_prev: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page pointing to URLs that return one of the 3xx (redirection) HTTP status codes")
    links_internal4xx: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes")
    links_internal4xx_prev: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page pointing to URLs that return one of the 4xx (client error) HTTP status codes")
    links_internal5xx: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes")
    links_internal5xx_prev: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page pointing to URLs that return one of the 5xx (server error) HTTP status codes")
    links_internal_follow: list[str | None] | None = Field(default=None, description="The list of internal outgoing dofollow links on the page")
    links_internal_follow_prev: list[str | None] | None = Field(default=None, description="The list of internal outgoing dofollow links on the page")
    links_internal_nofollow: list[str | None] | None = Field(default=None, description="The list of internal outgoing nofollow links on the page")
    links_internal_nofollow_prev: list[str | None] | None = Field(default=None, description="The list of internal outgoing nofollow links on the page")
    links_internal_non_canonical: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page that point to non-canonical pages")
    links_internal_non_canonical_prev: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page that point to non-canonical pages")
    links_internal_xxx: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code")
    links_internal_xxx_prev: list[str | None] | None = Field(default=None, description="The list of internal outgoing links on the page pointing to URLs that return HTTP status codes other than 2xx, 3xx, 4xx, 5xx or return no status code")
    links_js: list[str | None] | None = Field(default=None, description="The list of JavaScript files linked from the page")
    links_js_code: list[dict[str, Any] | None] | None = Field(default=None, description="The list of HTTP status codes returned by JavaScript files linked from the page")
    links_js_domain: list[str | None] | None = Field(default=None, description="The list of domains that contain JavaScript files linked from the page")
    links_js_domain_prev: list[str | None] | None = Field(default=None, description="The list of domains that contain JavaScript files linked from the page")
    links_js_prev: list[str | None] | None = Field(default=None, description="The list of JavaScript files linked from the page")
    links_js_scheme: list[str | None] | None = Field(default=None, description="The protocols of JavaScript files linked from the page")
    links_js_scheme_prev: list[str | None] | None = Field(default=None, description="The protocols of JavaScript files linked from the page")
    loading_time: int | None = Field(default=None, description="The time it takes for the crawler to load the full content of the document, measured in milliseconds")
    loading_time_diff: int | None = Field(default=None, description="The time it takes for the crawler to load the full content of the document, measured in milliseconds")
    loading_time_prev: int | None = Field(default=None, description="The time it takes for the crawler to load the full content of the document, measured in milliseconds")
    meta_description: list[str | None] | None = Field(default=None, description="Meta description")
    meta_description_length: list[int | None] | None = Field(default=None, description="Meta description length")
    meta_description_length_prev: list[int | None] | None = Field(default=None, description="Meta description length")
    meta_description_prev: list[str | None] | None = Field(default=None, description="Meta description")
    meta_refresh: list[str | None] | None = Field(default=None, description="The time set in a meta refresh tag, in seconds")
    meta_refresh_prev: list[str | None] | None = Field(default=None, description="The time set in a meta refresh tag, in seconds")
    meta_robots: list[str | None] | None = Field(default=None, description="Instructions for web crawlers specified in HTML robots meta tags on the page")
    meta_robots_prev: list[str | None] | None = Field(default=None, description="Instructions for web crawlers specified in HTML robots meta tags on the page")
    meta_twitter_tags_app_google_play: str | None = Field(default=None, description="The app ID in the Google Play Store specified in the twitter:app:id:ipad meta property")
    meta_twitter_tags_app_google_play_prev: str | None = Field(default=None, description="The app ID in the Google Play Store specified in the twitter:app:id:ipad meta property")
    meta_twitter_tags_app_ipad: str | None = Field(default=None, description="The app ID in the iTunes App Store specified in the twitter:app:id:ipad meta property")
    meta_twitter_tags_app_ipad_prev: str | None = Field(default=None, description="The app ID in the iTunes App Store specified in the twitter:app:id:ipad meta property")
    meta_twitter_tags_app_iphone: str | None = Field(default=None, description="The app ID in the iTunes App Store specified in the twitter:app:id:iphone meta property")
    meta_twitter_tags_app_iphone_prev: str | None = Field(default=None, description="The app ID in the iTunes App Store specified in the twitter:app:id:iphone meta property")
    meta_twitter_tags_attributes: list[str | None] | None = Field(default=None, description="The list of X (Twitter) Card properties on the page")
    meta_twitter_tags_attributes_prev: list[str | None] | None = Field(default=None, description="The list of X (Twitter) Card properties on the page")
    meta_twitter_tags_card: str | None = Field(default=None, description="The X (Twitter) Card type can be \"summary\", \"summary\\_large\\_image\", \"app\", or \"player\"")
    meta_twitter_tags_card_prev: str | None = Field(default=None, description="The X (Twitter) Card type can be \"summary\", \"summary\\_large\\_image\", \"app\", or \"player\"")
    meta_twitter_tags_description: str | None = Field(default=None, description="meta_twitter_tags.description")
    meta_twitter_tags_description_prev: str | None = Field(default=None, description="meta_twitter_tags.description")
    meta_twitter_tags_image: str | None = Field(default=None, description="The image URL specified in the twitter:image meta property")
    meta_twitter_tags_image_prev: str | None = Field(default=None, description="The image URL specified in the twitter:image meta property")
    meta_twitter_tags_image_url_invalid: bool | None = Field(default=None, description="Indicates that the URL specified in the twitter:image meta property is a valid absolute URL")
    meta_twitter_tags_image_url_invalid_prev: bool | None = Field(default=None, description="Indicates that the URL specified in the twitter:image meta property is a valid absolute URL")
    meta_twitter_tags_player: str | None = Field(default=None, description="The HTTPS URL of player iframe specified in the twitter:player meta property")
    meta_twitter_tags_player_height: int | None = Field(default=None, description="The height of iframe in pixels specified in the twitter:player:width meta property")
    meta_twitter_tags_player_height_diff: int | None = Field(default=None, description="The height of iframe in pixels specified in the twitter:player:width meta property")
    meta_twitter_tags_player_height_prev: int | None = Field(default=None, description="The height of iframe in pixels specified in the twitter:player:width meta property")
    meta_twitter_tags_player_prev: str | None = Field(default=None, description="The HTTPS URL of player iframe specified in the twitter:player meta property")
    meta_twitter_tags_player_width: int | None = Field(default=None, description="The width of iframe in pixels specified in the twitter:player:width meta property")
    meta_twitter_tags_player_width_diff: int | None = Field(default=None, description="The width of iframe in pixels specified in the twitter:player:width meta property")
    meta_twitter_tags_player_width_prev: int | None = Field(default=None, description="The width of iframe in pixels specified in the twitter:player:width meta property")
    meta_twitter_tags_site: str | None = Field(default=None, description="The X (Twitter) handle specified in the twitter:site meta property")
    meta_twitter_tags_site_prev: str | None = Field(default=None, description="The X (Twitter) handle specified in the twitter:site meta property")
    meta_twitter_tags_title: str | None = Field(default=None, description="The title text specified in the twitter:title meta property")
    meta_twitter_tags_title_prev: str | None = Field(default=None, description="The title text specified in the twitter:title meta property")
    meta_twitter_tags_valid: bool | None = Field(default=None, description="Indicates that the page has all the necessary tags required in a X (Twitter) Card")
    meta_twitter_tags_valid_prev: bool | None = Field(default=None, description="Indicates that the page has all the necessary tags required in a X (Twitter) Card")
    meta_twitter_tags_values: list[str | None] | None = Field(default=None, description="Data from the X (Twitter) Card properties on the page")
    meta_twitter_tags_values_prev: list[str | None] | None = Field(default=None, description="Data from the X (Twitter) Card properties on the page")
    navigation_next: str | None = Field(default=None, description="The URL specified in the rel=\"next\" element on the page")
    navigation_next_code: int | None = Field(default=None, description="The HTTP status code returned by the URL specified in the rel=\"next\" element on a page")
    navigation_next_no_crawl_reason: str | None = Field(default=None, description="The reason why the URL specified in the rel=\"next\" element on a page was not crawled")
    navigation_next_no_crawl_reason_prev: str | None = Field(default=None, description="The reason why the URL specified in the rel=\"next\" element on a page was not crawled")
    navigation_next_prev: str | None = Field(default=None, description="The URL specified in the rel=\"next\" element on the page")
    navigation_prev_code: int | None = Field(default=None, description="The HTTP status code returned by the URL specified in the rel=\"prev\" element on a page")
    navigation_prev_no_crawl_reason: str | None = Field(default=None, description="The reason why the URL specified in the rel=\"prev\" element on a page was not crawled")
    navigation_prev_no_crawl_reason_prev: str | None = Field(default=None, description="The reason why the URL specified in the rel=\"prev\" element on a page was not crawled")
    no_crawl_reason: str | None = Field(default=None, description="The reason why the URL was not crawled")
    no_crawl_reason_prev: str | None = Field(default=None, description="The reason why the URL was not crawled")
    nofollow: int | None = Field(default=None, description="The number of incoming external nofollow links pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    nofollow_diff: int | None = Field(default=None, description="The number of incoming external nofollow links pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    nofollow_prev: int | None = Field(default=None, description="The number of incoming external nofollow links pointing to the URL. Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    nr_h1: int | None = Field(default=None, description="The number of H1 subheaders on the page")
    nr_h1_prev: int | None = Field(default=None, description="The number of H1 subheaders on the page")
    nr_meta_description: int | None = Field(default=None, description="Number of Meta descriptions")
    nr_meta_description_diff: int | None = Field(default=None, description="Number of Meta descriptions")
    nr_meta_description_prev: int | None = Field(default=None, description="Number of Meta descriptions")
    nr_redirect_chain_urls: int | None = Field(default=None, description="The number of redirect chain URLs")
    nr_redirect_chain_urls_diff: int | None = Field(default=None, description="The number of redirect chain URLs")
    nr_redirect_chain_urls_prev: int | None = Field(default=None, description="The number of redirect chain URLs")
    nr_titles: int | None = Field(default=None, description="The number of title tags on the page")
    nr_titles_diff: int | None = Field(default=None, description="The number of title tags on the page")
    nr_titles_prev: int | None = Field(default=None, description="The number of title tags on the page")
    og_tags_attributes: list[str | None] | None = Field(default=None, description="The list of Open Graph properties on a page")
    og_tags_attributes_prev: list[str | None] | None = Field(default=None, description="The list of Open Graph properties on a page")
    og_tags_image: str | None = Field(default=None, description="The image URL specified in the og:image meta property")
    og_tags_image_prev: str | None = Field(default=None, description="The image URL specified in the og:image meta property")
    og_tags_image_url_invalid: bool | None = Field(default=None, description="Indicates that the URL specified in the og:image meta property is a valid absolute URL")
    og_tags_image_url_invalid_prev: bool | None = Field(default=None, description="Indicates that the URL specified in the og:image meta property is a valid absolute URL")
    og_tags_inconsistent_canonical: bool | None = Field(default=None, description="Indicates that the URL specified in the og:url meta property matches the URL specified as the canonical version of the page")
    og_tags_inconsistent_canonical_prev: bool | None = Field(default=None, description="Indicates that the URL specified in the og:url meta property matches the URL specified as the canonical version of the page")
    og_tags_title: str | None = Field(default=None, description="The title text specified in the og:title meta property")
    og_tags_title_prev: str | None = Field(default=None, description="The title text specified in the og:title meta property")
    og_tags_type: str | None = Field(default=None, description="The object type specified in the og:type meta property")
    og_tags_type_prev: str | None = Field(default=None, description="The object type specified in the og:type meta property")
    og_tags_url: str | None = Field(default=None, description="The URL specified in the og:url meta property")
    og_tags_url_prev: str | None = Field(default=None, description="The URL specified in the og:url meta property")
    og_tags_url_valid: bool | None = Field(default=None, description="Indicates that the URL specified in the og:url meta property is a valid absolute URL")
    og_tags_url_valid_prev: bool | None = Field(default=None, description="Indicates that the URL specified in the og:url meta property is a valid absolute URL")
    og_tags_valid: bool | None = Field(default=None, description="Indicates that the page has all four required Open Graph properties: og:title, og:type, og:image, and og:url")
    og_tags_valid_prev: bool | None = Field(default=None, description="Indicates that the page has all four required Open Graph properties: og:title, og:type, og:image, and og:url")
    og_tags_value: list[str | None] | None = Field(default=None, description="Data from Open Graph properties on a page")
    og_tags_value_prev: list[str | None] | None = Field(default=None, description="Data from Open Graph properties on a page")
    origin: str | None = Field(default=None, description="Shows where the URL was originally found during the crawl")
    origin_prev: str | None = Field(default=None, description="Shows where the URL was originally found during the crawl")
    page_is_nofollow: bool | None = Field(default=None, description="Check if the page is nofollow, based on http header and meta robots instructions")
    page_is_nofollow_prev: bool | None = Field(default=None, description="Check if the page is nofollow, based on http header and meta robots instructions")
    page_is_noindex: bool | None = Field(default=None, description="Check if the page is noindex, based on http header and meta robots instructions")
    page_is_noindex_prev: bool | None = Field(default=None, description="Check if the page is noindex, based on http header and meta robots instructions")
    page_rating: int | None = Field(default=None, description="Page Rating (PR) shows the URL's internal and external backlink profile strength relative to other URLs included in the crawl")
    page_raw_ur: int | None = Field(default=None, description="URL Rating (UR) shows the strength of your target page's backlink profile on a 100-point logarithmic scale. [Learn more](https://help.ahrefs.com/en/articles/72658-what-is-url-rating-ur)")
    page_raw_ur_diff: int | None = Field(default=None, description="URL Rating (UR) shows the strength of your target page's backlink profile on a 100-point logarithmic scale. [Learn more](https://help.ahrefs.com/en/articles/72658-what-is-url-rating-ur)")
    page_raw_ur_prev: int | None = Field(default=None, description="URL Rating (UR) shows the strength of your target page's backlink profile on a 100-point logarithmic scale. [Learn more](https://help.ahrefs.com/en/articles/72658-what-is-url-rating-ur)")
    page_type: list[str | None] | None = Field(default=None, description="Site Audit categorizes URLs as HTML Pages, Resource files (image, CSS or JavaScript), XML Sitemaps     and Robots.txt. If a page doesn't return status code 200 or has a content type that isn't covered by the categories above, it's     considered as \"Other\". Since we can't determine what these pages are, we further classify them based on how incoming links reference     them: as resources (receive resource incoming links) or as pages (receive non-resource incoming links)")
    page_type_prev: list[str | None] | None = Field(default=None, description="Site Audit categorizes URLs as HTML Pages, Resource files (image, CSS or JavaScript), XML Sitemaps     and Robots.txt. If a page doesn't return status code 200 or has a content type that isn't covered by the categories above, it's     considered as \"Other\". Since we can't determine what these pages are, we further classify them based on how incoming links reference     them: as resources (receive resource incoming links) or as pages (receive non-resource incoming links)")
    pagination_group: int | None = Field(default=None, description="The ID of the group of pages interconnected via their rel=\"next\" and rel=\"prev\" links")
    pagination_group_prev: int | None = Field(default=None, description="The ID of the group of pages interconnected via their rel=\"next\" and rel=\"prev\" links")
    positions: int | None = Field(default=None, description="The number of keywords the page is ranking for in top 100 organic search results worldwide (data from Ahrefs' Site Explorer)")
    positions_diff: int | None = Field(default=None, description="The number of keywords the page is ranking for in top 100 organic search results worldwide (data from Ahrefs' Site Explorer)")
    positions_prev: int | None = Field(default=None, description="The number of keywords the page is ranking for in top 100 organic search results worldwide (data from Ahrefs' Site Explorer)")
    positions_top10: int | None = Field(default=None, description="The number of keywords the page is ranking for in top 10 organic search results worldwide (data from Ahrefs' Site Explorer)")
    positions_top10_diff: int | None = Field(default=None, description="The number of keywords the page is ranking for in top 10 organic search results worldwide (data from Ahrefs' Site Explorer)")
    positions_top10_prev: int | None = Field(default=None, description="The number of keywords the page is ranking for in top 10 organic search results worldwide (data from Ahrefs' Site Explorer)")
    positions_top3: int | None = Field(default=None, description="The number of keywords the page is ranking for in top 3 organic search results worldwide (data from Ahrefs' Site Explorer)")
    positions_top3_diff: int | None = Field(default=None, description="The number of keywords the page is ranking for in top 3 organic search results worldwide (data from Ahrefs' Site Explorer)")
    positions_top3_prev: int | None = Field(default=None, description="The number of keywords the page is ranking for in top 3 organic search results worldwide (data from Ahrefs' Site Explorer)")
    psi_crux_cls_category: str | None = Field(default=None, description="Your CLS category will be either Good (<0.1), Needs Improvement (0.1 - 0.25), or Poor (>0.25). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_cls_category_prev: str | None = Field(default=None, description="Your CLS category will be either Good (<0.1), Needs Improvement (0.1 - 0.25), or Poor (>0.25). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_cls_distributions_proportion: list[dict[str, Any] | None] | None = Field(default=None, description="What % of collected CLS metrics are in each associated threshold, which categorize performance as either \"Good\", \"Needs Improvement\", or \"Poor\". [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_cls_distributions_proportion_prev: list[dict[str, Any] | None] | None = Field(default=None, description="What % of collected CLS metrics are in each associated threshold, which categorize performance as either \"Good\", \"Needs Improvement\", or \"Poor\". [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_cls_percentile: float | None = Field(default=None, description="Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_cls_percentile_diff: int | None = Field(default=None, description="Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_cls_percentile_prev: float | None = Field(default=None, description="Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_fid_category: str | None = Field(default=None, description="Your FID category will be either Good (<100 ms), Needs Improvement (100 ms - 300 ms), or Poor (>300 ms). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_fid_category_prev: str | None = Field(default=None, description="Your FID category will be either Good (<100 ms), Needs Improvement (100 ms - 300 ms), or Poor (>300 ms). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_fid_distributions_proportion: list[dict[str, Any] | None] | None = Field(default=None, description="What % of collected FID metrics are in each associated threshold, which categorize performance as either \"Good\", \"Needs Improvement\", or \"Poor\". [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_fid_distributions_proportion_prev: list[dict[str, Any] | None] | None = Field(default=None, description="What % of collected FID metrics are in each associated threshold, which categorize performance as either \"Good\", \"Needs Improvement\", or \"Poor\". [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_fid_percentile: float | None = Field(default=None, description="First Input Delay measures interactivity. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_fid_percentile_diff: int | None = Field(default=None, description="First Input Delay measures interactivity. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_fid_percentile_prev: float | None = Field(default=None, description="First Input Delay measures interactivity. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_inp_category: str | None = Field(default=None, description="Your INP category will be either Good (<200 ms), Needs Improvement (200 ms - 500 ms), or Poor (>500 ms). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://web.dev/inp/)")
    psi_crux_inp_category_prev: str | None = Field(default=None, description="Your INP category will be either Good (<200 ms), Needs Improvement (200 ms - 500 ms), or Poor (>500 ms). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://web.dev/inp/)")
    psi_crux_inp_distributions_proportion: list[dict[str, Any] | None] | None = Field(default=None, description="What % of collected INP metrics are in each associated threshold, which categorize performance as either \"Good\", \"Needs Improvement\", or \"Poor\". [Learn more](https://web.dev/inp/)")
    psi_crux_inp_distributions_proportion_prev: list[dict[str, Any] | None] | None = Field(default=None, description="What % of collected INP metrics are in each associated threshold, which categorize performance as either \"Good\", \"Needs Improvement\", or \"Poor\". [Learn more](https://web.dev/inp/)")
    psi_crux_inp_percentile: float | None = Field(default=None, description="Interaction to Next Paint measure overall responsiveness of a page to user interactions. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://web.dev/inp/)")
    psi_crux_inp_percentile_diff: int | None = Field(default=None, description="Interaction to Next Paint measure overall responsiveness of a page to user interactions. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://web.dev/inp/)")
    psi_crux_inp_percentile_prev: float | None = Field(default=None, description="Interaction to Next Paint measure overall responsiveness of a page to user interactions. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://web.dev/inp/)")
    psi_crux_lcp_category: str | None = Field(default=None, description="Your LCP category will be either Good (<2.5 sec), Needs Improvement (2.5 sec - 4.0 sec), or Poor (>4.0 sec). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_lcp_category_prev: str | None = Field(default=None, description="Your LCP category will be either Good (<2.5 sec), Needs Improvement (2.5 sec - 4.0 sec), or Poor (>4.0 sec). The category is based on the lowest threshold that includes 75% of page views. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_lcp_distributions_proportion: list[dict[str, Any] | None] | None = Field(default=None, description="What % of collected LCP metrics are in each associated threshold, which categorize performance as either \"Good\", \"Needs Improvement\", or \"Poor\". [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_lcp_distributions_proportion_prev: list[dict[str, Any] | None] | None = Field(default=None, description="What % of collected LCP metrics are in each associated threshold, which categorize performance as either \"Good\", \"Needs Improvement\", or \"Poor\". [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_lcp_percentile: float | None = Field(default=None, description="Largest Contentful Paint measures visual loading performance. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_lcp_percentile_diff: int | None = Field(default=None, description="Largest Contentful Paint measures visual loading performance. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_crux_lcp_percentile_prev: float | None = Field(default=None, description="Largest Contentful Paint measures visual loading performance. This score comes from the Chrome User Experience Report which looks at real user data. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_lighthouse_cls_error_message: str | None = Field(default=None, description="The message returned by Lighthouse if there is an error when measuring CLS")
    psi_lighthouse_cls_error_message_prev: str | None = Field(default=None, description="The message returned by Lighthouse if there is an error when measuring CLS")
    psi_lighthouse_cls_value: float | None = Field(default=None, description="Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_lighthouse_cls_value_diff: int | None = Field(default=None, description="Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_lighthouse_cls_value_prev: float | None = Field(default=None, description="Cumulative Layout Shift measures visual stability. The range is 0-1, where 0 is stable and 1 means a lot of shifting. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_lighthouse_lcp_error_message: str | None = Field(default=None, description="The message returned by Lighthouse if there is an error when measuring LCP")
    psi_lighthouse_lcp_error_message_prev: str | None = Field(default=None, description="The message returned by Lighthouse if there is an error when measuring LCP")
    psi_lighthouse_lcp_value: float | None = Field(default=None, description="Largest Contentful Paint measures visual loading performance. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_lighthouse_lcp_value_diff: int | None = Field(default=None, description="Largest Contentful Paint measures visual loading performance. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_lighthouse_lcp_value_prev: float | None = Field(default=None, description="Largest Contentful Paint measures visual loading performance. This score comes from Lighthouse in a simulated test environment. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_lighthouse_score: int | None = Field(default=None, description="This score uses multiple Lighthouse speed metrics to create a summary of the page's performance and use of best practices. Scores will be considered Good (>90), Needs Improvement (50-90), or Poor (<50). [Learn more](https://web.dev/performance-scoring/)")
    psi_lighthouse_score_diff: int | None = Field(default=None, description="This score uses multiple Lighthouse speed metrics to create a summary of the page's performance and use of best practices. Scores will be considered Good (>90), Needs Improvement (50-90), or Poor (<50). [Learn more](https://web.dev/performance-scoring/)")
    psi_lighthouse_score_prev: int | None = Field(default=None, description="This score uses multiple Lighthouse speed metrics to create a summary of the page's performance and use of best practices. Scores will be considered Good (>90), Needs Improvement (50-90), or Poor (<50). [Learn more](https://web.dev/performance-scoring/)")
    psi_lighthouse_tbt_error_message: str | None = Field(default=None, description="The message returned by Lighthouse if there is an error when measuring TBT")
    psi_lighthouse_tbt_error_message_prev: str | None = Field(default=None, description="The message returned by Lighthouse if there is an error when measuring TBT")
    psi_lighthouse_tbt_value: float | None = Field(default=None, description="Total Blocking Time measures the total amount of time that a page is blocked from responding to user interactions. This score comes from Lighthouse in a simulated test environment. TBT is the recommended alternative to FID for lab tests. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_lighthouse_tbt_value_diff: int | None = Field(default=None, description="Total Blocking Time measures the total amount of time that a page is blocked from responding to user interactions. This score comes from Lighthouse in a simulated test environment. TBT is the recommended alternative to FID for lab tests. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_lighthouse_tbt_value_prev: float | None = Field(default=None, description="Total Blocking Time measures the total amount of time that a page is blocked from responding to user interactions. This score comes from Lighthouse in a simulated test environment. TBT is the recommended alternative to FID for lab tests. [Learn more](https://ahrefs.com/blog/core-web-vitals/)")
    psi_mobile_issues: list[str | None] | None = Field(default=None, description="List of mobile-related issues on the page detected by Lighthouse")
    psi_mobile_issues_explanations: list[str | None] | None = Field(default=None, description="Details about the mobile issues detected by Lighthouse")
    psi_mobile_issues_explanations_prev: list[str | None] | None = Field(default=None, description="Details about the mobile issues detected by Lighthouse")
    psi_mobile_issues_prev: list[str | None] | None = Field(default=None, description="List of mobile-related issues on the page detected by Lighthouse")
    psi_request_error_message: str | None = Field(default=None, description="The message returned by PageSpeed Insights API if there is an error. [Learn more](https://help.ahrefs.com/en/articles/5369589-how-to-see-core-web-vitals-and-other-speed-metrics-in-site-audit-tool)")
    psi_request_error_message_prev: str | None = Field(default=None, description="The message returned by PageSpeed Insights API if there is an error. [Learn more](https://help.ahrefs.com/en/articles/5369589-how-to-see-core-web-vitals-and-other-speed-metrics-in-site-audit-tool)")
    psi_request_status: str | None = Field(default=None, description="The result of a request to PageSpeed Insights API. [Learn more](https://help.ahrefs.com/en/articles/5369589-how-to-see-core-web-vitals-and-other-speed-metrics-in-site-audit-tool)")
    psi_request_status_prev: str | None = Field(default=None, description="The result of a request to PageSpeed Insights API. [Learn more](https://help.ahrefs.com/en/articles/5369589-how-to-see-core-web-vitals-and-other-speed-metrics-in-site-audit-tool)")
    redirect: str | None = Field(default=None, description="The destination of the redirecting URL")
    redirect_chain_urls: list[str | None] | None = Field(default=None, description="The list of redirect chain URLs")
    redirect_chain_urls_code: list[dict[str, Any] | None] | None = Field(default=None, description="The list of HTTP status codes returned by the redirect chain URLs")
    redirect_chain_urls_no_crawl_reason: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why the redirect chain URLs were not crawled")
    redirect_chain_urls_no_crawl_reason_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The reasons why the redirect chain URLs were not crawled")
    redirect_chain_urls_prev: list[str | None] | None = Field(default=None, description="The list of redirect chain URLs")
    redirect_code: int | None = Field(default=None, description="The HTTP status code of the destination of the redirecting URL")
    redirect_counts: int | None = Field(default=None, description="The number of incoming external links pointing to the URL via a redirect. Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    redirect_counts_diff: int | None = Field(default=None, description="The number of incoming external links pointing to the URL via a redirect. Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    redirect_counts_prev: int | None = Field(default=None, description="The number of incoming external links pointing to the URL via a redirect. Not to be confused with the number of linking pages, as one page can contain multiple backlinks")
    redirect_is_canonical: bool | None = Field(default=None, description="Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical")
    redirect_is_canonical_prev: bool | None = Field(default=None, description="Indicates whether the target page tags itself as the canonical version to be shown in search results. A page is considered as canonical when it doesn't refer to any other pages as canonical")
    redirect_no_crawl_reason: str | None = Field(default=None, description="The reason why the destination of the redirecting URL was not crawled")
    redirect_no_crawl_reason_prev: str | None = Field(default=None, description="The reason why the destination of the redirecting URL was not crawled")
    redirect_prev: str | None = Field(default=None, description="The destination of the redirecting URL")
    redirect_scheme: str | None = Field(default=None, description="The protocol of the redirecting URL")
    redirect_scheme_prev: str | None = Field(default=None, description="The protocol of the redirecting URL")
    refclass_c: int | None = Field(default=None, description="The number of IP networks that have websites with at least 1 link pointing to the URL. An IP network consists of IP addresses sharing the first three numbers of their numerical label. Example: 151.80.39.61 is the website IP address where 151.80.39.XXX is the IP network")
    refclass_c_diff: int | None = Field(default=None, description="The number of IP networks that have websites with at least 1 link pointing to the URL. An IP network consists of IP addresses sharing the first three numbers of their numerical label. Example: 151.80.39.61 is the website IP address where 151.80.39.XXX is the IP network")
    refclass_c_prev: int | None = Field(default=None, description="The number of IP networks that have websites with at least 1 link pointing to the URL. An IP network consists of IP addresses sharing the first three numbers of their numerical label. Example: 151.80.39.61 is the website IP address where 151.80.39.XXX is the IP network")
    refhosts: int | None = Field(default=None, description="The number of unique external domains that have at least 1 link pointing to the URL (data from Ahrefs' Site Explorer database)")
    refhosts_diff: int | None = Field(default=None, description="The number of unique external domains that have at least 1 link pointing to the URL (data from Ahrefs' Site Explorer database)")
    refhosts_prev: int | None = Field(default=None, description="The number of unique external domains that have at least 1 link pointing to the URL (data from Ahrefs' Site Explorer database)")
    refips: int | None = Field(default=None, description="The number of unique external IP addresses that incorporate websites with at least 1 link pointing to the URL. Several domains can share one IP address")
    refips_prev: int | None = Field(default=None, description="The number of unique external IP addresses that incorporate websites with at least 1 link pointing to the URL. Several domains can share one IP address")
    refpages: int | None = Field(default=None, description="The number of unique external pages linking to the URL (data from Ahrefs' Site Explorer database)")
    refpages_diff: int | None = Field(default=None, description="The number of unique external pages linking to the URL (data from Ahrefs' Site Explorer database)")
    refpages_prev: int | None = Field(default=None, description="The number of unique external pages linking to the URL (data from Ahrefs' Site Explorer database)")
    robots_allow_rules: list[dict[str, Any] | None] | None = Field(default=None, description="Allow: rules")
    robots_allow_rules_prev: list[dict[str, Any] | None] | None = Field(default=None, description="Allow: rules")
    robots_crawl_delay: int | None = Field(default=None, description="Crawl-delay:")
    robots_crawl_delay_prev: int | None = Field(default=None, description="Crawl-delay:")
    robots_disallow_rules: list[dict[str, Any] | None] | None = Field(default=None, description="Disallow: rules")
    robots_disallow_rules_prev: list[dict[str, Any] | None] | None = Field(default=None, description="Disallow: rules")
    robots_error: str | None = Field(default=None, description="The error occurred while crawling the robots.txt file")
    robots_error_prev: str | None = Field(default=None, description="The error occurred while crawling the robots.txt file")
    robots_error_text: str | None = Field(default=None, description="Robots.txt error text")
    robots_error_text_prev: str | None = Field(default=None, description="Robots.txt error text")
    robots_redirect_loop: list[dict[str, Any] | None] | None = Field(default=None, description="Robots.txt error redirect loop")
    robots_redirect_loop_prev: list[dict[str, Any] | None] | None = Field(default=None, description="Robots.txt error redirect loop")
    robots_sitemaps: list[dict[str, Any] | None] | None = Field(default=None, description="The list of sitemaps referenced in the robots.txt file")
    robots_sitemaps_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The list of sitemaps referenced in the robots.txt file")
    rss: int | None = Field(default=None, description="The number of incoming external links from RSS feeds (data from Ahrefs' Site Explorer database)")
    rss_diff: int | None = Field(default=None, description="The number of incoming external links from RSS feeds (data from Ahrefs' Site Explorer database)")
    rss_prev: int | None = Field(default=None, description="The number of incoming external links from RSS feeds (data from Ahrefs' Site Explorer database)")
    scheme: str | None = Field(default=None, description="Hypertext Transfer Protocol of the URL (HTTP or HTTPS)")
    self_canonical: bool | None = Field(default=None, description="Indicates that the page has a self-referential canonical URL")
    self_canonical_prev: bool | None = Field(default=None, description="Indicates that the page has a self-referential canonical URL")
    self_hreflang: list[dict[str, Any] | None] | None = Field(default=None, description="Data from hreflang tag with a self-referential URL")
    self_hreflang_code_is_valid: list[dict[str, Any] | None] | None = Field(default=None, description="Indicates that hreflang data is specified properly in hreflang tag with a self-referential URL. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)")
    self_hreflang_code_is_valid_prev: list[dict[str, Any] | None] | None = Field(default=None, description="Indicates that hreflang data is specified properly in hreflang tag with a self-referential URL. The language must be specified in [ISO 639-1 format](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), and optionally the region in [ISO 3166-1 Alpha 2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)")
    self_hreflang_country: list[dict[str, Any] | None] | None = Field(default=None, description="The region specified in the hreflang tag with a self-referential URL")
    self_hreflang_country_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The region specified in the hreflang tag with a self-referential URL")
    self_hreflang_language: list[dict[str, Any] | None] | None = Field(default=None, description="The language specified in the hreflang tag with a self-referential URL")
    self_hreflang_language_prev: list[dict[str, Any] | None] | None = Field(default=None, description="The language specified in the hreflang tag with a self-referential URL")
    self_hreflang_prev: list[dict[str, Any] | None] | None = Field(default=None, description="Data from hreflang tag with a self-referential URL")
    serp_title: str | None = Field(default=None, description="The title displayed for the page in its top keyword's SERP on desktop")
    serp_title_prev: str | None = Field(default=None, description="The title displayed for the page in its top keyword's SERP on desktop")
    sitemap_error: str | None = Field(default=None, description="The error occurred while crawling the sitemap")
    sitemap_error_prev: str | None = Field(default=None, description="The error occurred while crawling the sitemap")
    sitemap_error_text: str | None = Field(default=None, description="Sitemap error text")
    sitemap_error_text_prev: str | None = Field(default=None, description="Sitemap error text")
    sitemap_is_index: bool | None = Field(default=None, description="Indicates that the sitemap is a sitemap index file")
    sitemap_is_index_prev: bool | None = Field(default=None, description="Indicates that the sitemap is a sitemap index file")
    sitemap_nr_urls: int | None = Field(default=None, description="The number of URLs referenced in the sitemap")
    sitemap_nr_urls_prev: int | None = Field(default=None, description="The number of URLs referenced in the sitemap")
    sitemap_save_max_size: int | None = Field(default=None, description="Max size of sitemap allows content to be saved")
    sitemap_save_max_size_diff: int | None = Field(default=None, description="Max size of sitemap allows content to be saved")
    sitemap_save_max_size_prev: int | None = Field(default=None, description="Max size of sitemap allows content to be saved")
    sitemap_unzipped_size: int | None = Field(default=None, description="Sitemap size (uncompressed)")
    sitemap_unzipped_size_diff: int | None = Field(default=None, description="Sitemap size (uncompressed)")
    sitemap_unzipped_size_prev: int | None = Field(default=None, description="Sitemap size (uncompressed)")
    size: int | None = Field(default=None, description="The size of the page or resource, measured in bytes")
    size_diff: int | None = Field(default=None, description="The size of the page or resource, measured in bytes")
    size_prev: int | None = Field(default=None, description="The size of the page or resource, measured in bytes")
    source: list[str | None] | None = Field(default=None, description="Source from which the URL can be reached")
    source_prev: list[str | None] | None = Field(default=None, description="Source from which the URL can be reached")
    stamp: str | None = Field(default=None, description="The time and date when the URL was crawled")
    stamp_prev: str | None = Field(default=None, description="The time and date when the URL was crawled")
    time_to_first_byte: int | None = Field(default=None, description="The time it takes for the crawler to receive the first byte of the response from a web server, measured in milliseconds")
    time_to_first_byte_prev: int | None = Field(default=None, description="The time it takes for the crawler to receive the first byte of the response from a web server, measured in milliseconds")
    title: list[str | None] | None = Field(default=None, description="The page title")
    title_prev: list[str | None] | None = Field(default=None, description="The page title")
    titles_length: list[int | None] | None = Field(default=None, description="The character length of the page title")
    titles_length_prev: list[int | None] | None = Field(default=None, description="The character length of the page title")
    top_keyword: str | None = Field(default=None, description="The keyword that brings the page the most organic traffic across all countries")
    top_keyword_position: int | None = Field(default=None, description="The position that the page holds for its top keyword")
    top_keyword_position_diff: int | None = Field(default=None, description="The position that the page holds for its top keyword")
    top_keyword_position_prev: int | None = Field(default=None, description="The position that the page holds for its top keyword")
    top_keyword_prev: str | None = Field(default=None, description="The keyword that brings the page the most organic traffic across all countries")
    traffic: float | None = Field(default=None, description="Our estimate of monthly organic search traffic coming to the URL (data from Ahrefs Site Explorer). Calculations are based on a mixture of clickstream data, the estimated monthly search volumes of keywords for which the page ranks, and the current ranking position for the URL in the search results. You can learn more [here](https://ahrefs.com/blog/ahrefs-seo-metrics/#organictraffic)")
    traffic_diff: float | None = Field(default=None, description="Our estimate of monthly organic search traffic coming to the URL (data from Ahrefs Site Explorer). Calculations are based on a mixture of clickstream data, the estimated monthly search volumes of keywords for which the page ranks, and the current ranking position for the URL in the search results. You can learn more [here](https://ahrefs.com/blog/ahrefs-seo-metrics/#organictraffic)")
    traffic_prev: float | None = Field(default=None, description="Our estimate of monthly organic search traffic coming to the URL (data from Ahrefs Site Explorer). Calculations are based on a mixture of clickstream data, the estimated monthly search volumes of keywords for which the page ranks, and the current ranking position for the URL in the search results. You can learn more [here](https://ahrefs.com/blog/ahrefs-seo-metrics/#organictraffic)")
    url: str | None = Field(default=None, description="The web address of the page or resource")
    url_prev: str | None = Field(default=None, description="The web address of the page or resource")


class SiteAuditPageExplorerResponse(BaseModel):
    """Response model for /page-explorer endpoint"""

    pages: list[SiteAuditPageExplorerData] | None = Field(default=None, description="The pages field")

    @property
    def data(self) -> list[SiteAuditPageExplorerData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-audit/projects
class SiteAuditProjectsRequest(BaseModel):
    """Request model for SiteAuditProjectsRequest."""

    date: str | None = Field(default=None, description="A timestamp in `YYYY-MM-DDThh:mm:ss` format specifying the crawl date to retrieve metrics from. Defaults to the most recent available crawl if omitted. For scheduled crawls, we return data from the latest crawl finished before the specified timestamp. For Always-on audit crawls, we return data as of the provided date and time. If the time component is omitted, it defaults to `00:00:00`. The timestamp is interpreted in UTC.")
    project_id: int | None = Field(default=None, description="The unique identifier of the project. You can find it in the URL of your Site Audit project in Ahrefs: `https://app.ahrefs.com/site-audit/#project_id#`")


class SiteAuditProjectsData(BaseModel):
    """Individual data item for /projects endpoint"""

    project_id: str | None = Field(default=None, description="The unique identifier of the project.")
    project_name: str | None = Field(default=None, description="The project name.")
    target_protocol: str | None = Field(default=None, description="The protocol of the target. Possible values: `both`, `http`, `https`.")
    target_url: str | None = Field(default=None, description="The URL of the project's target.")
    target_mode: str | None = Field(default=None, description="The scope of the target. Possible values: `exact`, `prefix`, `domain`, `subdomains`.")
    date: str | None = Field(default=None, description="The finish date and time of the last finished crawl, in GMT time zone.")
    status: str | None = Field(default=None, description="The status of the most recent finished crawl. Possible values: `Completed`, `Stopped`, `Error`, `In_progress`.")
    health_score: int | None = Field(default=None, description="Reflects the proportion of internal URLs on your site that do not have errors, based on the last finished crawl. Excludes crawls that are starting, in progress, finalizing, or were skipped.")
    urls_with_errors: int | None = Field(default=None, description="Number of internal URLs with errors")
    urls_with_warnings: int | None = Field(default=None, description="Number of internal URLs with warnings")
    urls_with_notices: int | None = Field(default=None, description="Number of internal URLs with notices")
    total: int | None = Field(default=None, description="Number of total crawled internal URLs")


class SiteAuditProjectsResponse(BaseModel):
    """Response model for /projects endpoint"""

    healthscores: list[SiteAuditProjectsData] | None = Field(default=None, description="The healthscores field")

    @property
    def data(self) -> list[SiteAuditProjectsData]:
        """Unwrap the response payload."""
        return self.healthscores or []


# ============== Site Explorer API ==============

# Models for site-explorer/all-backlinks
class SiteExplorerAllBacklinksRequest(BaseModel):
    """Request model for SiteExplorerAllBacklinksRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See the response schema for valid column identifiers, except for `link_group_count`, which is not supported in `order_by` for this endpoint.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    aggregation: AggregationEnum = Field(default=AggregationEnum.SIMILAR_LINKS, description="The backlinks grouping mode.")
    history: str = Field(default="all_time", description="A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format.")


class SiteExplorerAllBacklinksData(BaseModel):
    """Individual data item for /all-backlinks endpoint"""

    ahrefs_rank_source: int | None = Field(default=None, description="The strength of the referring domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.")
    ahrefs_rank_target: int | None = Field(default=None, description="The strength of the target domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.")
    alt: str | None = Field(default=None, description="The alt attribute of the link.")
    anchor: str | None = Field(default=None, description="The clickable words in a link that point to a URL.")
    broken_redirect_new_target: str | None = Field(default=None, description="The new destination of a modified redirect.")
    broken_redirect_reason: BrokenRedirectReasonEnum | None = Field(default=None, description="The reason the redirect was considered broken during the last crawl.")
    broken_redirect_source: str | None = Field(default=None, description="The redirecting URL that was modified, causing the redirect to become broken.")
    class_c: int | None = Field(default=None, description="(5 units) The number of unique class_c subnets linking to the referring page.")
    discovered_status: DiscoveredStatusEnum | None = Field(default=None, description="The reason the link was discovered during the last crawl: the page was crawled for the first time, the link was added to the page, or the link re-appeared after being removed.")
    domain_rating_source: float | None = Field(default=None, description="The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.")
    domain_rating_target: float | None = Field(default=None, description="The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.")
    drop_reason: DropReasonEnum | None = Field(default=None, description="The reason we removed the link from our index.")
    encoding: str | None = Field(default=None, description="The character set encoding of the referring page HTML.")
    first_seen: str | None = Field(default=None, description="The date the referring page URL was first discovered.")
    first_seen_link: str | None = Field(default=None, description="The date we first found a backlink to your target on a given referring page.")
    http_code: int | None = Field(default=None, description="The return code from HTTP protocol returned during the referring page crawl.")
    http_crawl: bool | None = Field(default=None, description="The link was discovered without executing javascript and rendering the page.")
    ip_source: str | None = Field(default=None, description="The referring domain IP address.")
    is_alternate: bool | None = Field(default=None, description="The link with the rel=“alternate” attribute.")
    is_canonical: bool | None = Field(default=None, description="The link with the rel=“canonical” attribute.")
    is_content: bool | None = Field(default=None, description="The link was found in the biggest piece of content on the page.")
    is_dofollow: bool | None = Field(default=None, description="The link has no special nofollow attribute.")
    is_form: bool | None = Field(default=None, description="The link was found in a form HTML tag.")
    is_frame: bool | None = Field(default=None, description="The link was found in an iframe HTML tag.")
    is_image: bool | None = Field(default=None, description="The link is a regular link that has an image inside their href attribute.")
    is_lost: bool | None = Field(default=None, description="The link currently does not exist anymore.")
    is_new: bool | None = Field(default=None, description="The link was discovered on the last crawl.")
    is_nofollow: bool | None = Field(default=None, description="The link or the referring page has the nofollow attribute set.")
    is_redirect: bool | None = Field(default=None, description="The link pointing to your target via a redirect.")
    is_redirect_lost: bool | None = Field(default=None, description="The redirected link currently does not exist anymore.")
    is_root_source: bool | None = Field(default=None, description="The referring domain name is a root domain name.")
    is_root_target: bool | None = Field(default=None, description="The target domain name is a root domain name.")
    is_rss: bool | None = Field(default=None, description="The link was found in an RSS feed.")
    is_spam: bool | None = Field(default=None, description="Indicates whether the backlink comes from a known spammy domain.")
    is_sponsored: bool | None = Field(default=None, description="The link has the Sponsored attribute set in the referring page HTML.")
    is_text: bool | None = Field(default=None, description="The link is a standard href hyperlink.")
    is_ugc: bool | None = Field(default=None, description="The link has the User Generated Content attribute set in the referring page HTML.")
    js_crawl: bool | None = Field(default=None, description="The link was discovered after executing javascript and rendering the page.")
    languages: list[str | None] | None = Field(default=None, description="The languages listed in the referring page metadata or detected by the crawler to appear in the HTML.")
    last_seen: str | None = Field(default=None, description="The date we discovered that the link was lost.")
    last_visited: str | None = Field(default=None, description="The date we last verified a live link to your target page.")
    link_group_count: int | None = Field(default=None, description="The number of backlinks that were grouped together based on the aggregation parameter. This field cannot be used with aggregation 'all'.")
    link_type: LinkTypeEnum | None = Field(default=None, description="The kind of the backlink.")
    linked_domains_source_domain: int | None = Field(default=None, description="The number of unique root domains linked from the referring domain.")
    linked_domains_source_page: int | None = Field(default=None, description="The number of unique root domains linked from the referring page.")
    linked_domains_target_domain: int | None = Field(default=None, description="The number of unique root domains linked from the target domain.")
    links_external: int | None = Field(default=None, description="The number of external links from the referring page.")
    links_internal: int | None = Field(default=None, description="The number of internal links from the referring page.")
    lost_reason: LostReasonEnum | None = Field(default=None, description="The reason the link was lost during the last crawl.")
    name_source: str | None = Field(default=None, description="The complete referring domain name, including subdomains.")
    name_target: str | None = Field(default=None, description="The complete target domain name, including subdomains.")
    noindex: bool | None = Field(default=None, description="The referring page has the noindex meta attribute.")
    page_size: int | None = Field(default=None, description="The size in bytes of the referring page content.")
    port_source: int | None = Field(default=None, description="The network port of the referring page URL.")
    port_target: int | None = Field(default=None, description="The network port of the target page URL.")
    positions: int | None = Field(default=None, description="The number of keywords that the referring page ranks for in the top 100 positions.")
    powered_by: list[str | None] | None = Field(default=None, description="Web technologies used to build and serve the referring page content.")
    redirect_code: int | None = Field(default=None, description="The HTTP status code of a referring page pointing to your target via a redirect.")
    redirect_kind: list[int | None] | None = Field(default=None, description="The HTTP status codes returned by the target redirecting URL or redirect chain.")
    refdomains_source: int | None = Field(default=None, description="(5 units) The number of unique referring domains linking to the referring page.")
    refdomains_source_domain: int | None = Field(default=None, description="(5 units) The number of unique referring domains linking to the referring domain.")
    refdomains_target_domain: int | None = Field(default=None, description="(5 units) The number of unique referring domains linking to the target domain.")
    root_name_source: str | None = Field(default=None, description="The root domain name of the referring domain, not including subdomains.")
    root_name_target: str | None = Field(default=None, description="The root domain name of the target domain, not including subdomains.")
    snippet_left: str | None = Field(default=None, description="The snippet of text appearing just before the link.")
    snippet_right: str | None = Field(default=None, description="The snippet of text appearing just after the link.")
    source_page_author: str | None = Field(default=None, description="The author of the referring page.")
    source_page_publish_date: str | None = Field(default=None, description="the date we identified the page was published")
    title: str | None = Field(default=None, description="The html title of the referring page.")
    tld_class_source: TldClassSourceEnum | None = Field(default=None, description="The top level domain class of the referring domain.")
    tld_class_target: TldClassSourceEnum | None = Field(default=None, description="The top level domain class of the target domain.")
    traffic: int | None = Field(default=None, description="(10 units) The referring page's estimated monthly organic traffic from search.")
    traffic_domain: int | None = Field(default=None, description="(10 units) The referring domain's estimated monthly organic traffic from search.")
    url_from: str | None = Field(default=None, description="The URL of the page containing a link to your target.")
    url_from_plain: str | None = Field(default=None, description="The referring page URL optimized for use as a filter.")
    url_rating_source: float | None = Field(default=None, description="The strength of the referring page's backlink profile compared to the others in our database on a 100-point scale.")
    url_redirect: list[str | None] | None = Field(default=None, description="A redirect chain the target URL of the link points to.")
    url_redirect_with_target: list[str | None] | None = Field(default=None, description="The target URL of the link with its redirect chain.")
    url_to: str | None = Field(default=None, description="The URL the backlink points to.")
    url_to_plain: str | None = Field(default=None, description="The target page URL optimized for use as a filter.")


class SiteExplorerAllBacklinksResponse(BaseModel):
    """Response model for /all-backlinks endpoint"""

    backlinks: list[SiteExplorerAllBacklinksData] | None = Field(default=None, description="The backlinks field")

    @property
    def data(self) -> list[SiteExplorerAllBacklinksData]:
        """Unwrap the response payload."""
        return self.backlinks or []


# Models for site-explorer/anchors
class SiteExplorerAnchorsRequest(BaseModel):
    """Request model for SiteExplorerAnchorsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    history: str = Field(default="all_time", description="A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format.")


class SiteExplorerAnchorsData(BaseModel):
    """Individual data item for /anchors endpoint"""

    anchor: str | None = Field(default=None, description="The clickable words in a link that point to a URL.")
    dofollow_links: int | None = Field(default=None, description="The number of links with a given anchor to your target that don’t have the “nofollow” attribute.")
    first_seen: str | None = Field(default=None, description="The date we first found a link with a given anchor to your target.")
    is_spam: bool | None = Field(default=None, description="Indicates whether the backlink comes from a known spammy domain.")
    last_seen: str | None = Field(default=None, description="The date we discovered the last backlink with a given anchor was lost.")
    links_to_target: int | None = Field(default=None, description="The number of inbound backlinks your target has with a given anchor.")
    lost_links: int | None = Field(default=None, description="The number of backlinks with a given anchor lost during the selected time period.")
    new_links: int | None = Field(default=None, description="The number of new backlinks with a given anchor found during the selected time period.")
    refdomains: int | None = Field(default=None, description="(5 units) The number of unique domains linking to your target with a given anchor.")
    refpages: int | None = Field(default=None, description="The number of pages containing a link with a given anchor to your target.")
    top_domain_rating: float | None = Field(default=None, description="The highest Domain Rating (DR) counted out of all referring domains. DR shows the strength of a website’s backlink profile compared to the others in our database on a 100-point scale.")


class SiteExplorerAnchorsResponse(BaseModel):
    """Response model for /anchors endpoint"""

    anchors: list[SiteExplorerAnchorsData] | None = Field(default=None, description="The anchors field")

    @property
    def data(self) -> list[SiteExplorerAnchorsData]:
        """Unwrap the response payload."""
        return self.anchors or []


# Models for site-explorer/backlinks-stats
class SiteExplorerBacklinksStatsRequest(BaseModel):
    """Request model for SiteExplorerBacklinksStatsRequest."""

    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")


class SiteExplorerBacklinksStatsData(BaseModel):
    """Individual data item for /backlinks-stats endpoint"""

    live: int | None = Field(default=None, description="The total number of links from other websites pointing to your target.")
    all_time: int | None = Field(default=None, description="The total number of links from other websites pointing to your target for all time.")
    live_refdomains: int | None = Field(default=None, description="(5 units) The total number of unique domains linking to your target.")
    all_time_refdomains: int | None = Field(default=None, description="(5 units) The total number of unique domains linking to your target for all time.")


class SiteExplorerBacklinksStatsResponse(BaseModel):
    """Response model for /backlinks-stats endpoint"""

    metrics: SiteExplorerBacklinksStatsData | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> SiteExplorerBacklinksStatsData | None:
        """Unwrap the response payload."""
        return self.metrics


# Models for site-explorer/best-by-external-links
class SiteExplorerBestByExternalLinksRequest(BaseModel):
    """Request model for SiteExplorerBestByExternalLinksRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See the response schema for valid column identifiers, except for `http_code_target`, `languages_target`, `last_visited_target`, `powered_by_target`, `target_redirect`, `title_target`, `url_rating_target`, which are not supported in `order_by` for this endpoint.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    history: str = Field(default="all_time", description="A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format.")


class SiteExplorerBestByExternalLinksData(BaseModel):
    """Individual data item for /best-by-external-links endpoint"""

    dofollow_to_target: int | None = Field(default=None, description="The number of links to your target page that don’t have the “nofollow” attribute.")
    first_seen_link: str | None = Field(default=None, description="The date we first found a link to your target.")
    http_code_target: int | None = Field(default=None, description="The return code from HTTP protocol returned during the target page crawl.")
    is_spam: bool | None = Field(default=None, description="Indicates whether the backlink comes from a known spammy domain.")
    languages_target: list[str | None] | None = Field(default=None, description="The languages listed in the target page metadata or detected by the crawler to appear in the HTML.")
    last_seen: str | None = Field(default=None, description="The date your target page lost its last live link.")
    last_visited_source: str | None = Field(default=None, description="The date we last verified a live link to your target page.")
    last_visited_target: str | None = Field(default=None, description="The date we last crawled your target page.")
    links_to_target: int | None = Field(default=None, description="The number of inbound backlinks the target page has.")
    lost_links_to_target: int | None = Field(default=None, description="The number of backlinks lost during the selected time period.")
    new_links_to_target: int | None = Field(default=None, description="The number of new backlinks found during the selected time period.")
    nofollow_to_target: int | None = Field(default=None, description="The number of links to your target page that have the “nofollow” attribute.")
    powered_by_target: list[str | None] | None = Field(default=None, description="Web technologies used to build and serve the target page content.")
    redirects_to_target: int | None = Field(default=None, description="The number of inbound redirects to your target page.")
    refdomains_target: int | None = Field(default=None, description="(5 units) The number of unique referring domains linking to the target page.")
    target_redirect: str | None = Field(default=None, description="The target's redirect if any.")
    title_target: str | None = Field(default=None, description="The html title of the target page.")
    top_domain_rating_source: float | None = Field(default=None, description="The highest Domain Rating (DR) counted out of all referring domains. DR shows the strength of a website’s backlink profile compared to the others in our database on a 100-point scale.")
    url_rating_target: float | None = Field(default=None, description="The strength of the target page's backlink profile compared to the others in our database on a 100-point scale.")
    url_to: str | None = Field(default=None, description="The URL the backlink points to.")
    url_to_plain: str | None = Field(default=None, description="The target page URL optimized for use as a filter.")


class SiteExplorerBestByExternalLinksResponse(BaseModel):
    """Response model for /best-by-external-links endpoint"""

    pages: list[SiteExplorerBestByExternalLinksData] | None = Field(default=None, description="The pages field")

    @property
    def data(self) -> list[SiteExplorerBestByExternalLinksData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-explorer/best-by-internal-links
class SiteExplorerBestByInternalLinksRequest(BaseModel):
    """Request model for SiteExplorerBestByInternalLinksRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")


class SiteExplorerBestByInternalLinksData(BaseModel):
    """Individual data item for /best-by-internal-links endpoint"""

    canonical_to_target: int | None = Field(default=None, description="The number of inbound canonical links to your target page.")
    dofollow_to_target: int | None = Field(default=None, description="The number of links to your target page that don’t have the “nofollow” attribute.")
    first_seen_link: str | None = Field(default=None, description="The date we first found a link to your target.")
    http_code_target: int | None = Field(default=None, description="The return code from HTTP protocol returned during the target page crawl.")
    languages_target: list[str | None] | None = Field(default=None, description="The languages listed in the target page metadata or detected by the crawler to appear in the HTML.")
    last_seen: str | None = Field(default=None, description="The date your target page lost its last live link.")
    last_visited_source: str | None = Field(default=None, description="The date we last verified a live link to your target page.")
    last_visited_target: str | None = Field(default=None, description="The date we last crawled your target page.")
    links_to_target: int | None = Field(default=None, description="The number of inbound backlinks the target page has.")
    nofollow_to_target: int | None = Field(default=None, description="The number of links to your target page that have the “nofollow” attribute.")
    powered_by_target: list[str | None] | None = Field(default=None, description="Web technologies used to build and serve the target page content.")
    redirects_to_target: int | None = Field(default=None, description="The number of inbound redirects to your target page.")
    target_redirect: str | None = Field(default=None, description="The target's redirect if any.")
    title_target: str | None = Field(default=None, description="The html title of the target page.")
    url_rating_target: float | None = Field(default=None, description="The strength of the target page's backlink profile compared to the others in our database on a 100-point scale.")
    url_to: str | None = Field(default=None, description="The URL the backlink points to.")
    url_to_plain: str | None = Field(default=None, description="The target page URL optimized for use as a filter.")


class SiteExplorerBestByInternalLinksResponse(BaseModel):
    """Response model for /best-by-internal-links endpoint"""

    pages: list[SiteExplorerBestByInternalLinksData] | None = Field(default=None, description="The pages field")

    @property
    def data(self) -> list[SiteExplorerBestByInternalLinksData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-explorer/broken-backlinks
class SiteExplorerBrokenBacklinksRequest(BaseModel):
    """Request model for SiteExplorerBrokenBacklinksRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See the response schema for valid column identifiers, except for `link_group_count`, `last_visited_target`, `http_code_target`, which are not supported in `order_by` for this endpoint.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    aggregation: AggregationEnum = Field(default=AggregationEnum.SIMILAR_LINKS, description="The backlinks grouping mode.")


class SiteExplorerBrokenBacklinksData(BaseModel):
    """Individual data item for /broken-backlinks endpoint"""

    ahrefs_rank_source: int | None = Field(default=None, description="The strength of the referring domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.")
    ahrefs_rank_target: int | None = Field(default=None, description="The strength of the target domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.")
    alt: str | None = Field(default=None, description="The alt attribute of the link.")
    anchor: str | None = Field(default=None, description="The clickable words in a link that point to a URL.")
    class_c: int | None = Field(default=None, description="(5 units) The number of unique class_c subnets linking to the referring page.")
    domain_rating_source: float | None = Field(default=None, description="The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.")
    domain_rating_target: float | None = Field(default=None, description="The strength of the referring domain's backlink profile compared to the others in our database on a 100-point scale.")
    encoding: str | None = Field(default=None, description="The character set encoding of the referring page HTML.")
    first_seen: str | None = Field(default=None, description="The date the referring page URL was first discovered.")
    first_seen_link: str | None = Field(default=None, description="The date we first found a backlink to your target on a given referring page.")
    http_code: int | None = Field(default=None, description="The return code from HTTP protocol returned during the referring page crawl.")
    http_code_target: int | None = Field(default=None, description="The return code from HTTP protocol returned during the target page crawl.")
    http_crawl: bool | None = Field(default=None, description="The link was discovered without executing javascript and rendering the page.")
    ip_source: str | None = Field(default=None, description="The referring domain IP address.")
    is_alternate: bool | None = Field(default=None, description="The link with the rel=“alternate” attribute.")
    is_canonical: bool | None = Field(default=None, description="The link with the rel=“canonical” attribute.")
    is_content: bool | None = Field(default=None, description="The link was found in the biggest piece of content on the page.")
    is_dofollow: bool | None = Field(default=None, description="The link has no special nofollow attribute.")
    is_form: bool | None = Field(default=None, description="The link was found in a form HTML tag.")
    is_frame: bool | None = Field(default=None, description="The link was found in an iframe HTML tag.")
    is_image: bool | None = Field(default=None, description="The link is a regular link that has an image inside their href attribute.")
    is_nofollow: bool | None = Field(default=None, description="The link or the referring page has the nofollow attribute set.")
    is_redirect: bool | None = Field(default=None, description="The link pointing to your target via a redirect.")
    is_root_source: bool | None = Field(default=None, description="The referring domain name is a root domain name.")
    is_root_target: bool | None = Field(default=None, description="The target domain name is a root domain name.")
    is_rss: bool | None = Field(default=None, description="The link was found in an RSS feed.")
    is_spam: bool | None = Field(default=None, description="Indicates whether the backlink comes from a known spammy domain.")
    is_sponsored: bool | None = Field(default=None, description="The link has the Sponsored attribute set in the referring page HTML.")
    is_text: bool | None = Field(default=None, description="The link is a standard href hyperlink.")
    is_ugc: bool | None = Field(default=None, description="The link has the User Generated Content attribute set in the referring page HTML.")
    js_crawl: bool | None = Field(default=None, description="The link was discovered after executing javascript and rendering the page.")
    languages: list[str | None] | None = Field(default=None, description="The languages listed in the referring page metadata or detected by the crawler to appear in the HTML.")
    last_seen: str | None = Field(default=None, description="The date we discovered that the link was lost.")
    last_visited: str | None = Field(default=None, description="The date we last re-crawled the referring page to verify the backlink is alive.")
    last_visited_target: str | None = Field(default=None, description="The date we last re-crawled the target page to verify that it is broken.")
    link_group_count: int | None = Field(default=None, description="The number of backlinks that were grouped together based on the aggregation parameter. This field cannot be used with aggregation 'all'.")
    link_type: LinkTypeEnum | None = Field(default=None, description="The kind of the backlink.")
    linked_domains_source_domain: int | None = Field(default=None, description="The number of unique root domains linked from the referring domain.")
    linked_domains_source_page: int | None = Field(default=None, description="The number of unique root domains linked from the referring page.")
    linked_domains_target_domain: int | None = Field(default=None, description="The number of unique root domains linked from the target domain.")
    links_external: int | None = Field(default=None, description="The number of external links from the referring page.")
    links_internal: int | None = Field(default=None, description="The number of internal links from the referring page.")
    name_source: str | None = Field(default=None, description="The complete referring domain name, including subdomains.")
    name_target: str | None = Field(default=None, description="The complete target domain name, including subdomains.")
    page_size: int | None = Field(default=None, description="The size in bytes of the referring page content.")
    port_source: int | None = Field(default=None, description="The network port of the referring page URL.")
    port_target: int | None = Field(default=None, description="The network port of the target page URL.")
    positions: int | None = Field(default=None, description="The number of keywords that the referring page ranks for in the top 100 positions.")
    powered_by: list[str | None] | None = Field(default=None, description="Web technologies used to build and serve the referring page content.")
    redirect_code: int | None = Field(default=None, description="The HTTP status code of a referring page pointing to your target via a redirect.")
    redirect_kind: list[int | None] | None = Field(default=None, description="The HTTP status codes returned by the target redirecting URL or redirect chain.")
    refdomains_source: int | None = Field(default=None, description="(5 units) The number of unique referring domains linking to the referring page.")
    refdomains_source_domain: int | None = Field(default=None, description="(5 units) The number of unique referring domains linking to the referring domain.")
    refdomains_target_domain: int | None = Field(default=None, description="(5 units) The number of unique referring domains linking to the target domain.")
    root_name_source: str | None = Field(default=None, description="The root domain name of the referring domain, not including subdomains.")
    root_name_target: str | None = Field(default=None, description="The root domain name of the target domain, not including subdomains.")
    snippet_left: str | None = Field(default=None, description="The snippet of text appearing just before the link.")
    snippet_right: str | None = Field(default=None, description="The snippet of text appearing just after the link.")
    source_page_author: str | None = Field(default=None, description="The author of the referring page.")
    title: str | None = Field(default=None, description="The html title of the referring page.")
    tld_class_source: TldClassSourceEnum | None = Field(default=None, description="The top level domain class of the referring domain.")
    tld_class_target: TldClassSourceEnum | None = Field(default=None, description="The top level domain class of the target domain.")
    traffic: int | None = Field(default=None, description="(10 units) The referring page's estimated monthly organic traffic from search.")
    traffic_domain: int | None = Field(default=None, description="(10 units) The referring domain's estimated monthly organic traffic from search.")
    url_from: str | None = Field(default=None, description="The URL of the page containing a link to your target.")
    url_from_plain: str | None = Field(default=None, description="The referring page URL optimized for use as a filter.")
    url_rating_source: float | None = Field(default=None, description="The strength of the referring page's backlink profile compared to the others in our database on a 100-point scale.")
    url_redirect: list[str | None] | None = Field(default=None, description="A redirect chain the target URL of the link points to.")
    url_redirect_with_target: list[str | None] | None = Field(default=None, description="The target URL of the link with its redirect chain.")
    url_to: str | None = Field(default=None, description="The URL the backlink points to.")
    url_to_plain: str | None = Field(default=None, description="The target page URL optimized for use as a filter.")


class SiteExplorerBrokenBacklinksResponse(BaseModel):
    """Response model for /broken-backlinks endpoint"""

    backlinks: list[SiteExplorerBrokenBacklinksData] | None = Field(default=None, description="The backlinks field")

    @property
    def data(self) -> list[SiteExplorerBrokenBacklinksData]:
        """Unwrap the response payload."""
        return self.backlinks or []


# Models for site-explorer/domain-rating
class SiteExplorerDomainRatingRequest(BaseModel):
    """Request model for SiteExplorerDomainRatingRequest."""

    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")


class SiteExplorerDomainRatingData(BaseModel):
    """Individual data item for /domain-rating endpoint"""

    domain_rating: float | None = Field(default=None, description="The strength of your target's backlink profile compared to the other websites in our database on a 100-point logarithmic scale.")
    ahrefs_rank: int | None = Field(default=None, description="The strength of your target's backlink profile compared to the other websites in our database, with rank #1 being the strongest.")


class SiteExplorerDomainRatingResponse(BaseModel):
    """Response model for /domain-rating endpoint"""

    domain_rating: SiteExplorerDomainRatingData | None = Field(default=None, description="The domain_rating field")

    @property
    def data(self) -> SiteExplorerDomainRatingData | None:
        """Unwrap the response payload."""
        return self.domain_rating


# Models for site-explorer/domain-rating-history
class SiteExplorerDomainRatingHistoryRequest(BaseModel):
    """Request model for SiteExplorerDomainRatingHistoryRequest."""

    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY, description="The time interval used to group historical data.")
    date_to: DateStr | None = Field(default=None, description="The end date of the historical period in YYYY-MM-DD format.")
    date_from: DateStr = Field(..., description="The start date of the historical period in YYYY-MM-DD format.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")


class SiteExplorerDomainRatingHistoryData(BaseModel):
    """Individual data item for /domain-rating-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    domain_rating: float | None = Field(default=None, description="The strength of your target page's backlink profile compared to the other websites in our database on a 100-point logarithmic scale.")


class SiteExplorerDomainRatingHistoryResponse(BaseModel):
    """Response model for /domain-rating-history endpoint"""

    domain_ratings: list[SiteExplorerDomainRatingHistoryData] | None = Field(default=None, description="The domain_ratings field")

    @property
    def data(self) -> list[SiteExplorerDomainRatingHistoryData]:
        """Unwrap the response payload."""
        return self.domain_ratings or []


# Models for site-explorer/keywords-history
class SiteExplorerKeywordsHistoryRequest(BaseModel):
    """Request model for SiteExplorerKeywordsHistoryRequest."""

    select: SelectStr = Field(default="date,top3,top4_10,top11_plus", description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY, description="The time interval used to group historical data.")
    date_to: DateStr | None = Field(default=None, description="The end date of the historical period in YYYY-MM-DD format.")
    date_from: DateStr = Field(..., description="The start date of the historical period in YYYY-MM-DD format.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")


class SiteExplorerKeywordsHistoryData(BaseModel):
    """Individual data item for /keywords-history endpoint"""

    date: str | None = Field(default=None)
    top11_20: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 11-20 organic search results.")
    top11_plus: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 11+ organic search results.")
    top21_50: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 21-50 organic search results.")
    top3: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 3 organic search results.")
    top4_10: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 4-10 organic search results.")
    top51_plus: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 51+ organic search results.")


class SiteExplorerKeywordsHistoryResponse(BaseModel):
    """Response model for /keywords-history endpoint"""

    keywords: list[SiteExplorerKeywordsHistoryData] | None = Field(default=None, description="The keywords field")

    @property
    def data(self) -> list[SiteExplorerKeywordsHistoryData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for site-explorer/linked-anchors-external
class SiteExplorerLinkedAnchorsExternalRequest(BaseModel):
    """Request model for SiteExplorerLinkedAnchorsExternalRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")


class SiteExplorerLinkedAnchorsExternalData(BaseModel):
    """Individual data item for /linked-anchors-external endpoint"""

    anchor: str | None = Field(default=None, description="The clickable words in a link that point to a URL.")
    dofollow_links: int | None = Field(default=None, description="The number of outbound links with a given anchor from your target that don’t have the “nofollow” attribute.")
    first_seen: str | None = Field(default=None, description="The date we first found a link with a given anchor on your target.")
    linked_domains: int | None = Field(default=None, description="The number of unique domains linked from your target with a given anchor.")
    linked_pages: int | None = Field(default=None, description="The number of unique pages linked from your target with a given anchor.")
    links_from_target: int | None = Field(default=None, description="The number of outbound links your target has with a given anchor.")


class SiteExplorerLinkedAnchorsExternalResponse(BaseModel):
    """Response model for /linked-anchors-external endpoint"""

    linkedanchors: list[SiteExplorerLinkedAnchorsExternalData] | None = Field(default=None, description="The linkedanchors field")

    @property
    def data(self) -> list[SiteExplorerLinkedAnchorsExternalData]:
        """Unwrap the response payload."""
        return self.linkedanchors or []


# Models for site-explorer/linked-anchors-internal
class SiteExplorerLinkedAnchorsInternalRequest(BaseModel):
    """Request model for SiteExplorerLinkedAnchorsInternalRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")


class SiteExplorerLinkedAnchorsInternalData(BaseModel):
    """Individual data item for /linked-anchors-internal endpoint"""

    anchor: str | None = Field(default=None, description="The clickable words in a link that point to a URL.")
    dofollow_links: int | None = Field(default=None, description="The number of outbound links with a given anchor from your target that don’t have the “nofollow” attribute.")
    first_seen: str | None = Field(default=None, description="The date we first found a link with a given anchor on your target.")
    linked_pages: int | None = Field(default=None, description="The number of unique pages linked from your target with a given anchor.")
    links_from_target: int | None = Field(default=None, description="The number of outbound links your target has with a given anchor.")


class SiteExplorerLinkedAnchorsInternalResponse(BaseModel):
    """Response model for /linked-anchors-internal endpoint"""

    linkedanchors: list[SiteExplorerLinkedAnchorsInternalData] | None = Field(default=None, description="The linkedanchors field")

    @property
    def data(self) -> list[SiteExplorerLinkedAnchorsInternalData]:
        """Unwrap the response payload."""
        return self.linkedanchors or []


# Models for site-explorer/linkeddomains
class SiteExplorerLinkeddomainsRequest(BaseModel):
    """Request model for SiteExplorerLinkeddomainsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")


class SiteExplorerLinkeddomainsData(BaseModel):
    """Individual data item for /linkeddomains endpoint"""

    dofollow_linked_domains: int | None = Field(default=None, description="The number of unique root domains with dofollow links linked from the linked domain.")
    dofollow_links: int | None = Field(default=None, description="The number of links from your target to the linked domain that don’t have the “nofollow” attribute.")
    dofollow_refdomains: int | None = Field(default=None, description="(5 units) The number of unique domains with dofollow links to the linked domain.")
    domain: str | None = Field(default=None, description="A linked domain that has at least one link from your target.")
    domain_rating: float | None = Field(default=None, description="The strength of a domain's backlink profile compared to the others in our database on a 100-point scale.")
    first_seen: str | None = Field(default=None, description="The date we first found a link to the linked domain from your target.")
    is_root_domain: bool | None = Field(default=None, description="The domain name is a root domain name.")
    linked_domain_traffic: int | None = Field(default=None, description="(10 units) The linked domain’s estimated monthly organic traffic from search")
    linked_pages: int | None = Field(default=None, description="The number of the domain's pages linked from your target.")
    links_from_target: int | None = Field(default=None, description="The number of links to the linked domain from your target.")


class SiteExplorerLinkeddomainsResponse(BaseModel):
    """Response model for /linkeddomains endpoint"""

    linkeddomains: list[SiteExplorerLinkeddomainsData] | None = Field(default=None, description="The linkeddomains field")

    @property
    def data(self) -> list[SiteExplorerLinkeddomainsData]:
        """Unwrap the response payload."""
        return self.linkeddomains or []


# Models for site-explorer/metrics
class SiteExplorerMetricsRequest(BaseModel):
    """Request model for SiteExplorerMetricsRequest."""

    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")


class SiteExplorerMetricsData(BaseModel):
    """Individual data item for /metrics endpoint"""

    org_keywords: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 100 organic search results.")
    paid_keywords: int | None = Field(default=None, description="The total number of keywords that your target ranks for in paid search results.")
    org_keywords_1_3: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 3 organic search results.")
    org_traffic: int | None = Field(default=None, description="(10 units) The estimated number of monthly visitors that your target gets from organic search.")
    org_cost: int | None = Field(default=None, description="(10 units) The estimated value of your target's monthly organic search traffic, in USD cents.")
    paid_traffic: int | None = Field(default=None, description="(10 units) The estimated number of monthly visitors that your target gets from paid search.")
    paid_cost: int | None = Field(default=None, description="(10 units) The estimated cost of your target's monthly paid search traffic, in USD cents.")
    paid_pages: int | None = Field(default=None, description="The total number of pages from a target ranking in paid search results.")


class SiteExplorerMetricsResponse(BaseModel):
    """Response model for /metrics endpoint"""

    metrics: SiteExplorerMetricsData | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> SiteExplorerMetricsData | None:
        """Unwrap the response payload."""
        return self.metrics


# Models for site-explorer/metrics-by-country
class SiteExplorerMetricsByCountryRequest(BaseModel):
    """Request model for SiteExplorerMetricsByCountryRequest."""

    select: SelectStr = Field(default="paid_cost,paid_keywords,org_cost,paid_pages,org_keywords_1_3,org_keywords,org_traffic,paid_traffic,country", description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")


class SiteExplorerMetricsByCountryData(BaseModel):
    """Individual data item for /metrics-by-country endpoint"""

    country: CountryEnum1 | None = Field(default=None, description="The country field")
    org_cost: int | None = Field(default=None, description="(10 units) The estimated value of your target's monthly organic search traffic, in USD cents.")
    org_keywords: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 100 organic search results.")
    org_keywords_1_3: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 3 organic search results.")
    org_traffic: int | None = Field(default=None, description="(10 units) The estimated number of monthly visitors that your target gets from organic search.")
    paid_cost: int | None = Field(default=None, description="(10 units) The estimated cost of your target's monthly paid search traffic, in USD cents.")
    paid_keywords: int | None = Field(default=None, description="The total number of keywords that your target ranks for in paid search results.")
    paid_pages: int | None = Field(default=None, description="The total number of pages from a target ranking in the top 100 paid search results.")
    paid_traffic: int | None = Field(default=None, description="(10 units) The estimated number of monthly visitors that your target gets from paid search.")


class SiteExplorerMetricsByCountryResponse(BaseModel):
    """Response model for /metrics-by-country endpoint"""

    metrics: list[SiteExplorerMetricsByCountryData] | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> list[SiteExplorerMetricsByCountryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for site-explorer/metrics-history
class SiteExplorerMetricsHistoryRequest(BaseModel):
    """Request model for SiteExplorerMetricsHistoryRequest."""

    select: SelectStr = Field(default="date,org_cost,org_traffic,paid_cost,paid_traffic", description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")
    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY, description="The time interval used to group historical data.")
    date_to: DateStr | None = Field(default=None, description="The end date of the historical period in YYYY-MM-DD format.")
    date_from: DateStr = Field(..., description="The start date of the historical period in YYYY-MM-DD format.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")


class SiteExplorerMetricsHistoryData(BaseModel):
    """Individual data item for /metrics-history endpoint"""

    date: str | None = Field(default=None)
    org_cost: int | None = Field(default=None, description="(10 units) The estimated cost of your target's monthly organic search traffic, in USD cents.")
    org_traffic: int | None = Field(default=None, description="(10 units) The estimated number of monthly visitors that your target gets from organic search.")
    paid_cost: int | None = Field(default=None, description="(10 units) The estimated cost of your target's monthly paid search traffic, in USD cents.")
    paid_traffic: int | None = Field(default=None, description="(10 units) The estimated number of monthly visitors that your target gets from paid search.")


class SiteExplorerMetricsHistoryResponse(BaseModel):
    """Response model for /metrics-history endpoint"""

    metrics: list[SiteExplorerMetricsHistoryData] | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> list[SiteExplorerMetricsHistoryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for site-explorer/organic-competitors
class SiteExplorerOrganicCompetitorsRequest(BaseModel):
    """Request model for SiteExplorerOrganicCompetitorsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    country: CountryEnum = Field(..., description="A two-letter country code (ISO 3166-1 alpha-2).")
    date_compared: DateStr | None = Field(default=None, description="A date to compare metrics with in YYYY-MM-DD format.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")


class SiteExplorerOrganicCompetitorsData(BaseModel):
    """Individual data item for /organic-competitors endpoint"""

    competitor_domain: str | None = Field(default=None, description="A competitor's domain of your target in “domains\" group mode.")
    competitor_url: str | None = Field(default=None, description="A competitor's URL of your target in pages\" group mode.")
    domain_rating: float | None = Field(default=None, description="The strength of a domain's backlink profile compared to the others in our database on a 100-point scale.")
    group_mode: GroupModeEnum | None = Field(default=None, description="To see competing pages instead, use the “exact URL” target mode or “path” target mode if your target doesn't have multiple pages.")
    keywords_common: int | None = Field(default=None, description="Organic keywords that both your target and a competitor are ranking for.")
    keywords_competitor: int | None = Field(default=None, description="Organic keywords that a competitor is ranking for, but your target isn't.")
    keywords_target: int | None = Field(default=None, description="Organic keywords that your target is ranking for, but a competitor isn't.")
    pages: int | None = Field(default=None, description="The total number of pages from a target ranking in search results.")
    pages_diff: int | None = Field(default=None, description="The change in pages between your selected dates.")
    pages_merged: int | None = Field(default=None, description="The pages field optimized for sorting.")
    pages_prev: int | None = Field(default=None, description="The total number of pages from a target ranking in search results on the comparison date.")
    share: float | None = Field(default=None, description="The percentage of common keywords out of the total number of keywords that your target and a competitor both rank for.")
    traffic: int | None = Field(default=None, description="(10 units) An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the \"volume_mode\" parameter.")
    traffic_diff: int | None = Field(default=None, description="The change in traffic between your selected dates.")
    traffic_merged: int | None = Field(default=None, description="(10 units) The traffic field optimized for sorting.")
    traffic_prev: int | None = Field(default=None, description="(10 units) An estimation of the number of monthly visits that a page gets from organic search over the latest month or over the latest known 12 months of data depending on the \"volume_mode\" parameter on the comparison date.")
    value: int | None = Field(default=None, description="(10 units) The estimated value of a page's monthly organic search traffic, in USD cents.")
    value_diff: int | None = Field(default=None, description="The change in value between your selected dates.")
    value_merged: int | None = Field(default=None, description="(10 units) The value field optimized for sorting.")
    value_prev: int | None = Field(default=None, description="(10 units) The estimated value of a page's monthly organic search traffic, in USD cents on the comparison date.")


class SiteExplorerOrganicCompetitorsResponse(BaseModel):
    """Response model for /organic-competitors endpoint"""

    competitors: list[SiteExplorerOrganicCompetitorsData] | None = Field(default=None, description="The competitors field")

    @property
    def data(self) -> list[SiteExplorerOrganicCompetitorsData]:
        """Unwrap the response payload."""
        return self.competitors or []


# Models for site-explorer/organic-keywords
class SiteExplorerOrganicKeywordsRequest(BaseModel):
    """Request model for SiteExplorerOrganicKeywordsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    date_compared: DateStr | None = Field(default=None, description="A date to compare metrics with in YYYY-MM-DD format.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")


class SiteExplorerOrganicKeywordsData(BaseModel):
    """Individual data item for /organic-keywords endpoint"""

    all_positions: list[dict[str, Any] | None] | None = Field(default=None, description="(5 units) The list of all positions for a keyword.")
    all_positions_prev: list[dict[str, Any] | None] | None = Field(default=None, description="(5 units) The list of all positions for a keyword on the comparison date.")
    best_position: int | None = Field(default=None, description="The top position your target ranks for in the organic search results for a keyword.")
    best_position_diff: int | None = Field(default=None, description="The change in position between your selected dates.")
    best_position_has_thumbnail: bool | None = Field(default=None, description="The top position has a thumbnail.")
    best_position_has_thumbnail_prev: bool | None = Field(default=None, description="The top position has a thumbnail on the comparison date.")
    best_position_has_video: bool | None = Field(default=None, description="The top position has a video.")
    best_position_has_video_prev: bool | None = Field(default=None, description="The top position has a video on the comparison date.")
    best_position_kind: BestPositionKindEnum | None = Field(default=None, description="The kind of the top position: organic, paid, or a SERP feature.")
    best_position_kind_merged: BestPositionKindEnum | None = Field(default=None, description="The kind of the top position optimized for sorting.")
    best_position_kind_prev: BestPositionKindEnum | None = Field(default=None, description="The kind of the top position on the comparison date.")
    best_position_prev: int | None = Field(default=None, description="The top position on the comparison date.")
    best_position_set: BestPositionSetEnum | None = Field(default=None, description="The ranking group of the top position.")
    best_position_set_prev: BestPositionSetEnum | None = Field(default=None, description="The ranking group of the top position on the comparison date.")
    best_position_url: str | None = Field(default=None, description="The ranking URL in organic search results.")
    best_position_url_prev: str | None = Field(default=None, description="The ranking URL on the comparison date.")
    cpc: int | None = Field(default=None, description="Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in USD cents.")
    cpc_merged: int | None = Field(default=None, description="The CPC field optimized for sorting.")
    cpc_prev: int | None = Field(default=None, description="The CPC metric on the comparison date.")
    entities: list[dict[str, Any] | None] | None = Field(default=None, description="Organizations, products, persons, works, events, and locations found in a keyword.")
    is_best_position_set_top_11_50: bool | None = Field(default=None, description="The ranking group of the top position is 11-50.")
    is_best_position_set_top_11_50_prev: bool | None = Field(default=None, description="The ranking group of the top position was 11-50 on the comparison date.")
    is_best_position_set_top_3: bool | None = Field(default=None, description="The ranking group of the top position is Top 3.")
    is_best_position_set_top_3_prev: bool | None = Field(default=None, description="The ranking group of the top position was Top 3 on the comparison date.")
    is_best_position_set_top_4_10: bool | None = Field(default=None, description="The ranking group of the top position is 4-10.")
    is_best_position_set_top_4_10_prev: bool | None = Field(default=None, description="The ranking group of the top position was 4-10 on the comparison date.")
    is_branded: bool | None = Field(default=None, description="User intent: branded. The user is searching for a specific brand or company name.")
    is_commercial: bool | None = Field(default=None, description="User intent: commercial. The user is comparing products or services before making a purchase decision.")
    is_informational: bool | None = Field(default=None, description="User intent: informational. The user is looking for information or an answer to a specific question.")
    is_local: bool | None = Field(default=None, description="User intent: local. The user is looking for information relevant to a specific location or nearby services.")
    is_navigational: bool | None = Field(default=None, description="User intent: navigational. The user is searching for a specific website or web page.")
    is_transactional: bool | None = Field(default=None, description="User intent: transactional. The user is ready to complete an action, often a purchase.")
    keyword: str | None = Field(default=None, description="The keyword your target ranks for.")
    keyword_country: CountryEnum1 | None = Field(default=None, description="The country of a keyword your target ranks for.")
    keyword_difficulty: int | None = Field(default=None, description="(10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.")
    keyword_difficulty_merged: int | None = Field(default=None, description="(10 units) The keyword difficulty field optimized for sorting.")
    keyword_difficulty_prev: int | None = Field(default=None, description="(10 units) The keyword difficulty on the comparison date.")
    keyword_merged: str | None = Field(default=None, description="The keyword field optimized for sorting.")
    keyword_prev: str | None = Field(default=None, description="The keyword your target ranks for on the comparison date.")
    language: str | None = Field(default=None, description="The SERP language.")
    language_prev: str | None = Field(default=None, description="The SERP language on the comparison date.")
    last_update: str | None = Field(default=None, description="The date when we last checked search engine results for a keyword.")
    last_update_prev: str | None = Field(default=None, description="The date when we checked search engine results up to the comparison date.")
    serp_features: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None, description="The SERP features that appear in search results for a keyword.")
    serp_features_count: int | None = Field(default=None, description="The number of SERP features that appear in search results for a keyword.")
    serp_features_count_prev: int | None = Field(default=None, description="The number of SERP features on the comparison date.")
    serp_features_merged: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None, description="The SERP features field optimized for sorting.")
    serp_features_prev: list[SerpFeaturesItemEnum1 | None] | None = Field(default=None, description="The SERP features that appear in search results for a keyword on the comparison date.")
    serp_target_main_positions_count: int | None = Field(default=None, description="The number of target URLs ranking for a keyword excluding positions in Sitelinks, Top stories, Image packs, and posts on X (Twitter).")
    serp_target_main_positions_count_prev: int | None = Field(default=None, description="The number of target URLs ranking for a keyword excluding positions in Sitelinks, Top stories, Image packs, and posts on X (Twitter) on the comparison date.")
    serp_target_positions_count: int | None = Field(default=None, description="The number of target URLs ranking for a keyword.")
    serp_target_positions_count_prev: int | None = Field(default=None, description="The number of target URLs ranking for a keyword on the comparison date.")
    status: StatusEnum | None = Field(default=None, description="The status of a page: the new page that just started to rank (\"left\"), the lost page that disappeared from search results (\"right\"), or no change (\"both\").")
    sum_paid_traffic: int | None = Field(default=None, description="(10 units) An estimation of the number of monthly visits that your target gets from paid search for a keyword.")
    sum_paid_traffic_merged: int | None = Field(default=None, description="(10 units) The paid traffic field optimized for sorting.")
    sum_paid_traffic_prev: int | None = Field(default=None, description="(10 units) The paid traffic on the comparison date.")
    sum_traffic: int | None = Field(default=None, description="(10 units) An estimation of the number of monthly visitors that your target gets from organic search for a keyword.")
    sum_traffic_merged: int | None = Field(default=None, description="(10 units) The traffic field optimized for sorting.")
    sum_traffic_prev: int | None = Field(default=None, description="(10 units) The traffic on the comparison date.")
    volume: int | None = Field(default=None, description="(10 units) An estimation of the number of searches for a keyword over the latest month.")
    volume_desktop_pct: float | None = Field(default=None, description="The percentage of the total search volume that comes from desktop devices.")
    volume_merged: int | None = Field(default=None, description="(10 units) The search volume field optimized for sorting.")
    volume_mobile_pct: float | None = Field(default=None, description="The percentage of the total search volume that comes from mobile devices.")
    volume_prev: int | None = Field(default=None, description="(10 units) The search volume on the comparison date.")
    words: int | None = Field(default=None, description="The number of words in a keyword.")
    words_merged: int | None = Field(default=None, description="The number of words in a keyword optimized for sorting.")
    words_prev: int | None = Field(default=None, description="The number of words in a keyword on the comparison date.")


class SiteExplorerOrganicKeywordsResponse(BaseModel):
    """Response model for /organic-keywords endpoint"""

    keywords: list[SiteExplorerOrganicKeywordsData] | None = Field(default=None, description="The keywords field")

    @property
    def data(self) -> list[SiteExplorerOrganicKeywordsData]:
        """Unwrap the response payload."""
        return self.keywords or []


# Models for site-explorer/outlinks-stats
class SiteExplorerOutlinksStatsRequest(BaseModel):
    """Request model for SiteExplorerOutlinksStatsRequest."""

    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")


class SiteExplorerOutlinksStatsData(BaseModel):
    """Individual data item for /outlinks-stats endpoint"""

    outgoing_links: int | None = Field(default=None, description="The number of external links from the target.")
    outgoing_links_dofollow: int | None = Field(default=None, description="The number of external dofollow links from the target.")
    linked_domains: int | None = Field(default=None, description="The number of unique root domains linked from the target.")
    linked_domains_dofollow: int | None = Field(default=None, description="The number of unique root domains linked via dofollow links from the target.")


class SiteExplorerOutlinksStatsResponse(BaseModel):
    """Response model for /outlinks-stats endpoint"""

    metrics: SiteExplorerOutlinksStatsData | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> SiteExplorerOutlinksStatsData | None:
        """Unwrap the response payload."""
        return self.metrics


# Models for site-explorer/pages-by-traffic
class SiteExplorerPagesByTrafficRequest(BaseModel):
    """Request model for SiteExplorerPagesByTrafficRequest."""

    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")


class SiteExplorerPagesByTrafficData(BaseModel):
    """Individual data item for /pages-by-traffic endpoint"""

    range0_pages: int | None = Field(default=None, description="The total number of pages with 0 traffic.")
    range100_traffic: int | None = Field(default=None, description="(10 units) The total traffic from pages with 1-100 traffic.")
    range100_pages: int | None = Field(default=None, description="The total number of pages with 1-100 traffic.")
    range1k_traffic: int | None = Field(default=None, description="(10 units) The total traffic from pages with 101-1K traffic.")
    range1k_pages: int | None = Field(default=None, description="The total number of pages with 101-1K traffic.")
    range5k_traffic: int | None = Field(default=None, description="(10 units) The total traffic from pages with 1K-5K traffic.")
    range5k_pages: int | None = Field(default=None, description="The total number of pages with 1K-5K traffic.")
    range10k_traffic: int | None = Field(default=None, description="(10 units) The total traffic from pages with 5K-10K traffic.")
    range10k_pages: int | None = Field(default=None, description="The total number of pages with 5K-10K traffic.")
    range10k_plus_traffic: int | None = Field(default=None, description="(10 units) The total traffic from pages with 10K+ traffic.")
    range10k_plus_pages: int | None = Field(default=None, description="The total number of pages with 10K+ traffic.")


class SiteExplorerPagesByTrafficResponse(BaseModel):
    """Response model for /pages-by-traffic endpoint"""

    pages: SiteExplorerPagesByTrafficData | None = Field(default=None, description="The pages field")

    @property
    def data(self) -> SiteExplorerPagesByTrafficData | None:
        """Unwrap the response payload."""
        return self.pages


# Models for site-explorer/pages-history
class SiteExplorerPagesHistoryRequest(BaseModel):
    """Request model for SiteExplorerPagesHistoryRequest."""

    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY, description="The time interval used to group historical data.")
    date_to: DateStr | None = Field(default=None, description="The end date of the historical period in YYYY-MM-DD format.")
    date_from: DateStr = Field(..., description="The start date of the historical period in YYYY-MM-DD format.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")


class SiteExplorerPagesHistoryData(BaseModel):
    """Individual data item for /pages-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    pages: int | None = Field(default=None, description="The total number of pages from a target ranking in the top 100 organic search results.")


class SiteExplorerPagesHistoryResponse(BaseModel):
    """Response model for /pages-history endpoint"""

    pages: list[SiteExplorerPagesHistoryData] | None = Field(default=None, description="The pages field")

    @property
    def data(self) -> list[SiteExplorerPagesHistoryData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-explorer/paid-pages
class SiteExplorerPaidPagesRequest(BaseModel):
    """Request model for SiteExplorerPaidPagesRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    date_compared: DateStr | None = Field(default=None, description="A date to compare metrics with in YYYY-MM-DD format.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")


class SiteExplorerPaidPagesData(BaseModel):
    """Individual data item for /paid-pages endpoint"""

    ads_count: int | None = Field(default=None, description="The number of unique ads with a page.")
    ads_count_diff: int | None = Field(default=None, description="The change in ads between your selected dates.")
    ads_count_prev: int | None = Field(default=None, description="The number of ads on the comparison date.")
    keywords: int | None = Field(default=None, description="The total number of keywords that your target ranks for in paid search results.")
    keywords_diff: int | None = Field(default=None, description="The change in keywords between your selected dates.")
    keywords_diff_percent: int | None = Field(default=None, description="The change in keywords between your selected dates, in percents.")
    keywords_merged: int | None = Field(default=None, description="The total number of keywords optimized for sorting.")
    keywords_prev: int | None = Field(default=None, description="The keyword your target ranks for on the comparison date.")
    raw_url: str | None = Field(default=None, description="The ranking page URL in encoded format.")
    raw_url_prev: str | None = Field(default=None, description="The ranking page URL on the comparison date in encoded format.")
    referring_domains: int | None = Field(default=None, description="(5 units) The number of unique domains linking to a page.")
    status: StatusEnum | None = Field(default=None, description="The status of a page: the new page that just started to rank in paid results (\"left\"), the lost page that disappeared from paid results (\"right\"), or no change (\"both\").")
    sum_traffic: int | None = Field(default=None, description="(10 units) An estimation of the monthly paid search traffic that a page gets from all the keywords that it ranks for.")
    sum_traffic_merged: int | None = Field(default=None, description="(10 units) The paid traffic field optimized for sorting.")
    sum_traffic_prev: int | None = Field(default=None, description="(10 units) The paid traffic on the comparison date.")
    top_keyword: str | None = Field(default=None, description="The keyword that brings the most paid traffic to a page.")
    top_keyword_best_position: int | None = Field(default=None, description="The ranking position that a page holds for its top keyword.")
    top_keyword_best_position_diff: int | None = Field(default=None, description="The change in the top position between your selected dates.")
    top_keyword_best_position_kind: BestPositionKindEnum | None = Field(default=None, description="The kind of the top position: organic, paid or a SERP feature.")
    top_keyword_best_position_kind_prev: BestPositionKindEnum | None = Field(default=None, description="The kind of the top position on the comparison date.")
    top_keyword_best_position_prev: int | None = Field(default=None, description="The top position on the comparison date.")
    top_keyword_best_position_title: str | None = Field(default=None, description="The title displayed for the page in its top keyword's SERP.")
    top_keyword_best_position_title_prev: str | None = Field(default=None, description="The title displayed for the page in its top keyword's SERP on the comparison date.")
    top_keyword_country: CountryEnum1 | None = Field(default=None, description="The country in which a page ranks for its top keyword.")
    top_keyword_country_prev: CountryEnum1 | None = Field(default=None, description="The country in which a page ranks for its top keyword on the comparison date.")
    top_keyword_prev: str | None = Field(default=None, description="The keyword that brings the most paid traffic to a page on the comparison date.")
    top_keyword_volume: int | None = Field(default=None, description="(10 units) An estimation of the average monthly number of searches for the top keyword over the latest month or over the latest known 12 months of data depending on the \"volume_mode\" parameter.")
    top_keyword_volume_prev: int | None = Field(default=None, description="(10 units) The search volume on the comparison date.")
    traffic_diff: int | None = Field(default=None, description="The change in traffic between your selected dates.")
    traffic_diff_percent: int | None = Field(default=None, description="The change in traffic between your selected dates, in percents.")
    ur: float | None = Field(default=None, description="URL Rating (UR) shows the strength of your target page’s backlink profile on a 100-point logarithmic scale.")
    url: str | None = Field(default=None, description="The ranking page URL.")
    url_prev: str | None = Field(default=None, description="The ranking page URL on the comparison date.")
    value: int | None = Field(default=None, description="(10 units) The estimated cost of a page's monthly paid search traffic, in USD cents.")
    value_diff: int | None = Field(default=None, description="The change in traffic value between your selected dates.")
    value_diff_percent: int | None = Field(default=None, description="The change in traffic value between your selected dates, in percents.")
    value_merged: int | None = Field(default=None, description="(10 units) The traffic value field optimized for sorting.")
    value_prev: int | None = Field(default=None, description="(10 units) The traffic value on the comparison date.")


class SiteExplorerPaidPagesResponse(BaseModel):
    """Response model for /paid-pages endpoint"""

    pages: list[SiteExplorerPaidPagesData] | None = Field(default=None, description="The pages field")

    @property
    def data(self) -> list[SiteExplorerPaidPagesData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-explorer/refdomains
class SiteExplorerRefdomainsRequest(BaseModel):
    """Request model for SiteExplorerRefdomainsRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    history: str = Field(default="all_time", description="A time frame to add lost backlinks to the report. Choose between `live` (no history), `since:<date>` (history since a specified date), and `all_time` (full history). The date should be in YYYY-MM-DD format.")


class SiteExplorerRefdomainsData(BaseModel):
    """Individual data item for /refdomains endpoint"""

    dofollow_linked_domains: int | None = Field(default=None, description="The number of unique root domains with dofollow links linked from the referring domain.")
    dofollow_links: int | None = Field(default=None, description="The number of links from the referring domain to your target that don't have the “nofollow” attribute.")
    dofollow_refdomains: int | None = Field(default=None, description="(5 units) The number of unique domains with dofollow links to the referring domain.")
    domain: str | None = Field(default=None, description="A referring domain that has at least one link to your target.")
    domain_rating: float | None = Field(default=None, description="The strength of a domain's backlink profile compared to the others in our database on a 100-point scale.")
    first_seen: str | None = Field(default=None, description="The date we first found a backlink to your target from the referring domain.")
    ip_source: str | None = Field(default=None, description="The referring domain IP address.")
    is_root_domain: bool | None = Field(default=None, description="The domain name is a root domain name.")
    is_spam: bool | None = Field(default=None, description="Indicates whether the backlink comes from a known spammy domain.")
    last_seen: str | None = Field(default=None, description="The date your target lost its last live backlink for the referring domain.")
    links_to_target: int | None = Field(default=None, description="The number of backlinks from the referring domain to your target.")
    lost_links: int | None = Field(default=None, description="The number of backlinks lost from the referring domain for the selected time period.")
    new_links: int | None = Field(default=None, description="The number of new backlinks found from the referring domain for the selected time period.")
    positions_source_domain: int | None = Field(default=None, description="The number of keywords that the referring domain ranks for in the top 100 positions.")
    traffic_domain: int | None = Field(default=None, description="(10 units) The referring domain's estimated monthly organic traffic from search.")


class SiteExplorerRefdomainsResponse(BaseModel):
    """Response model for /refdomains endpoint"""

    refdomains: list[SiteExplorerRefdomainsData] | None = Field(default=None, description="The refdomains field")

    @property
    def data(self) -> list[SiteExplorerRefdomainsData]:
        """Unwrap the response payload."""
        return self.refdomains or []


# Models for site-explorer/refdomains-history
class SiteExplorerRefdomainsHistoryRequest(BaseModel):
    """Request model for SiteExplorerRefdomainsHistoryRequest."""

    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY, description="The time interval used to group historical data.")
    date_to: DateStr | None = Field(default=None, description="The end date of the historical period in YYYY-MM-DD format.")
    date_from: DateStr = Field(..., description="The start date of the historical period in YYYY-MM-DD format.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")


class SiteExplorerRefdomainsHistoryData(BaseModel):
    """Individual data item for /refdomains-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    refdomains: int | None = Field(default=None, description="(5 units) The total number of unique domains linking to your target.")


class SiteExplorerRefdomainsHistoryResponse(BaseModel):
    """Response model for /refdomains-history endpoint"""

    refdomains: list[SiteExplorerRefdomainsHistoryData] | None = Field(default=None, description="The refdomains field")

    @property
    def data(self) -> list[SiteExplorerRefdomainsHistoryData]:
        """Unwrap the response payload."""
        return self.refdomains or []


# Models for site-explorer/top-pages
class SiteExplorerTopPagesRequest(BaseModel):
    """Request model for SiteExplorerTopPagesRequest."""

    timeout: int | None = Field(default=None, description="A manual timeout duration in seconds.")
    limit: int = Field(default=1000, description="The number of results to return.")
    order_by: str | None = Field(default=None, description="A column to order results by. See response schema for valid column identifiers.")
    where: str | None = Field(default=None, description="Filter expression. See filter-syntax.md for syntax.")
    select: SelectStr = Field(..., description="A comma-separated list of columns to return. See response schema for valid column identifiers.")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    date_compared: DateStr | None = Field(default=None, description="A date to compare metrics with in YYYY-MM-DD format.")
    date: DateStr = Field(..., description="A date to report metrics on in YYYY-MM-DD format.")
    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")


class SiteExplorerTopPagesData(BaseModel):
    """Individual data item for /top-pages endpoint"""

    keywords: int | None = Field(default=None, description="The total number of keywords that your target ranks for in the top 100 organic search results.")
    keywords_diff: int | None = Field(default=None, description="The change in keywords between your selected dates.")
    keywords_diff_percent: int | None = Field(default=None, description="The change in keywords between your selected dates, in percents.")
    keywords_merged: int | None = Field(default=None, description="The total number of keywords optimized for sorting.")
    keywords_prev: int | None = Field(default=None, description="The keyword your target ranks for on the comparison date.")
    raw_url: str | None = Field(default=None, description="The ranking page URL in encoded format.")
    raw_url_prev: str | None = Field(default=None, description="The ranking page URL on the comparison date in encoded format.")
    referring_domains: int | None = Field(default=None, description="(5 units) The number of unique domains linking to a page.")
    status: StatusEnum | None = Field(default=None, description="The status of a page: the new page that just started to rank (\"left\"), the lost page that disappeared from search results (\"right\"), or no change (\"both\").")
    sum_traffic: int | None = Field(default=None, description="(10 units) An estimation of the monthly organic search traffic that a page gets from all the keywords that it ranks for.")
    sum_traffic_merged: int | None = Field(default=None, description="(10 units) The traffic field optimized for sorting.")
    sum_traffic_prev: int | None = Field(default=None, description="(10 units) The traffic on the comparison date.")
    top_keyword: str | None = Field(default=None, description="The keyword that brings the most organic traffic to a page.")
    top_keyword_best_position: int | None = Field(default=None, description="The ranking position that a page holds for its top keyword.")
    top_keyword_best_position_diff: int | None = Field(default=None, description="The change in the top position between your selected dates.")
    top_keyword_best_position_kind: BestPositionKindEnum | None = Field(default=None, description="The kind of the top position: organic, paid or a SERP feature.")
    top_keyword_best_position_kind_prev: BestPositionKindEnum | None = Field(default=None, description="The kind of the top position on the comparison date.")
    top_keyword_best_position_prev: int | None = Field(default=None, description="The top position on the comparison date.")
    top_keyword_best_position_title: str | None = Field(default=None, description="The title displayed for the page in its top keyword's SERP.")
    top_keyword_best_position_title_prev: str | None = Field(default=None, description="The title displayed for the page in its top keyword's SERP on the comparison date.")
    top_keyword_country: CountryEnum1 | None = Field(default=None, description="The country in which a page ranks for its top keyword.")
    top_keyword_country_prev: CountryEnum1 | None = Field(default=None, description="The country in which a page ranks for its top keyword on the comparison date.")
    top_keyword_prev: str | None = Field(default=None, description="The keyword that brings the most organic traffic to a page on the comparison date.")
    top_keyword_volume: int | None = Field(default=None, description="(10 units) An estimation of the average monthly number of searches for the top keyword over the latest month or over the latest known 12 months of data depending on the \"volume_mode\" parameter.")
    top_keyword_volume_prev: int | None = Field(default=None, description="(10 units) The search volume on the comparison date.")
    traffic_diff: int | None = Field(default=None, description="The change in traffic between your selected dates.")
    traffic_diff_percent: int | None = Field(default=None, description="The change in traffic between your selected dates, in percents.")
    ur: float | None = Field(default=None, description="URL Rating (UR) shows the strength of your target page’s backlink profile on a 100-point logarithmic scale.")
    url: str | None = Field(default=None, description="The ranking page URL.")
    url_prev: str | None = Field(default=None, description="The ranking page URL on the comparison date.")
    value: int | None = Field(default=None, description="(10 units) The estimated value of a page's monthly organic search traffic, in USD cents.")
    value_diff: int | None = Field(default=None, description="The change in traffic value between your selected dates.")
    value_diff_percent: int | None = Field(default=None, description="The change in traffic value between your selected dates, in percents.")
    value_merged: int | None = Field(default=None, description="(10 units) The traffic value field optimized for sorting.")
    value_prev: int | None = Field(default=None, description="(10 units) The traffic value on the comparison date.")


class SiteExplorerTopPagesResponse(BaseModel):
    """Response model for /top-pages endpoint"""

    pages: list[SiteExplorerTopPagesData] | None = Field(default=None, description="The pages field")

    @property
    def data(self) -> list[SiteExplorerTopPagesData]:
        """Unwrap the response payload."""
        return self.pages or []


# Models for site-explorer/total-search-volume-history
class SiteExplorerTotalSearchVolumeHistoryRequest(BaseModel):
    """Request model for SiteExplorerTotalSearchVolumeHistoryRequest."""

    volume_mode: VolumeModeEnum = Field(default=VolumeModeEnum.MONTHLY, description="The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value.")
    top_positions: ViewForEnum = Field(default=ViewForEnum.TOP_10, description="The number of top organic search positions to consider when calculating total search volume.")
    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY, description="The time interval used to group historical data.")
    date_to: DateStr | None = Field(default=None, description="The end date of the historical period in YYYY-MM-DD format.")
    date_from: DateStr = Field(..., description="The start date of the historical period in YYYY-MM-DD format.")
    country: CountryEnum | None = Field(default=None, description="A two-letter country code (ISO 3166-1 alpha-2).")
    protocol: ProtocolEnum = Field(default=ProtocolEnum.BOTH, description="The protocol of your target.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    mode: ModeEnum = Field(default=ModeEnum.SUBDOMAINS, description="The scope of the search based on the target you entered.")


class SiteExplorerTotalSearchVolumeHistoryData(BaseModel):
    """Individual data item for /total-search-volume-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    total_search_volume: int | None = Field(default=None, description="(10 units) The total search volume of keywords for which your target ranks within the specified `top_positions` in the search results.")


class SiteExplorerTotalSearchVolumeHistoryResponse(BaseModel):
    """Response model for /total-search-volume-history endpoint"""

    metrics: list[SiteExplorerTotalSearchVolumeHistoryData] | None = Field(default=None, description="The metrics field")

    @property
    def data(self) -> list[SiteExplorerTotalSearchVolumeHistoryData]:
        """Unwrap the response payload."""
        return self.metrics or []


# Models for site-explorer/url-rating-history
class SiteExplorerUrlRatingHistoryRequest(BaseModel):
    """Request model for SiteExplorerUrlRatingHistoryRequest."""

    history_grouping: HistoryGroupingEnum = Field(default=HistoryGroupingEnum.MONTHLY, description="The time interval used to group historical data.")
    date_to: DateStr | None = Field(default=None, description="The end date of the historical period in YYYY-MM-DD format.")
    date_from: DateStr = Field(..., description="The start date of the historical period in YYYY-MM-DD format.")
    target: str = Field(..., description="The target of the search: a domain or a URL.")


class SiteExplorerUrlRatingHistoryData(BaseModel):
    """Individual data item for /url-rating-history endpoint"""

    date: str | None = Field(default=None, description="The date field")
    url_rating: float | None = Field(default=None, description="The strength of your target page's backlink profile compared to the other websites in our database on a 100-point logarithmic scale.")


class SiteExplorerUrlRatingHistoryResponse(BaseModel):
    """Response model for /url-rating-history endpoint"""

    url_ratings: list[SiteExplorerUrlRatingHistoryData] | None = Field(default=None, description="The url_ratings field")

    @property
    def data(self) -> list[SiteExplorerUrlRatingHistoryData]:
        """Unwrap the response payload."""
        return self.url_ratings or []

