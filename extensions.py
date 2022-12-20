class Extensions:
    def __init__(self):
        self.image_extensions = set(["jpg", "jpeg", "png", "gif", "bmp", "svg", "tiff", "webp", "ico", "psd", "raw", "arw", "cr2", "nrw", "k25", "dib", "heif", "heic", "ind", "indd", "indt", "jp2", "j2k", "jpf", "jpf", "jpx", "jpm", "mj2", "ai", "eps"])
        self.video_extensions = set(["mkv", "webm", "mpg", "mp2", "mpeg", "mpe", "mpv", "ogg", "mp4", "mp4v", "m4v", "avi", "wmv", "mov", "qt", "flv", "swf", "avchd"])
        self.document_extensions = set(["epub", "txt", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "odt", "ods", "odp", "rtf", "tex", "wks", "wps", "wpd", "htm"])
        self.software_extensions = set(["xpi", "whl", "exe", "msi", "apk", "bat", "bin", "cgi", "pl", "com", "gadget", "jar", "wsf", "vb", "vbs", "pyw", "sh", "cmd", "deb", "rpm", "run", "msu", "msp", "msix", "msixbundle", "appx", "appxbundle", "ps1", "ps1xml", "ps2", "ps2xml", "psc1", "psc2", "msh", "msh1", "msh2", "mshxml", "msh1xml", "msh2xml", "scf", "lnk", "inf", "reg", "dll", "cfg", "cpl", "cur", "deskthemepack", "dll", "dmp", "drv", "icns", "ico", "lnk", "sys", "cfg", "ini", "prf"])
        self.iso_extensions = set(["iso", "img", "vcd"])
        self.archived_extensions = set(["7z", "arj", "deb", "pkg", "rar", "rpm", "tar.gz", "z", "zip", "gz"])
        self.torrent_extensions = set(["torrent"])
        self.codefiles_extensions = set(["ipynb", "ts", "c", "class", "cpp", "cs", "h", "java", "sh", "swift", "vb", "js", "pl", "py", "html", "css", "php", "rb", "asp", "aspx", "cgi", "pl", "rss", "xhtml"])
        self.audio_extensions = set(["aif", "cda", "mid", "midi", "mp3", "mpa", "ogg", "wav", "wma", "wpl"])
        self.datafiles_extensions = set(["csv", "dat", "db", "dbf", "log", "mdb", "sav", "sql", "tar", "xml", "json", "ttf"])
