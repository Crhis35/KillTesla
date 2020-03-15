html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>{%title%}</title>
                            {%favicon%}
                            {%css%}
                            <link rel="stylesheet" href="../static/dist/css/styles.css">
                            <link rel="stylesheet" href="../static/dist/css/style.css">
                        </head>
                        <body>
                            <header>
                                <span class="icon"><img class='logo' src="../static/dist/img/logo.svg" alt="logo"></span>
                                <nav>
                                    <ul class="nav__links">
                                        <li><a href="/">Home</a></li>
                                        <li><a href="#">DriveM</a></li>
                                        <li><a href="#">SelfDrive</a></li>
                                        <li><a href="/dashapp/">Graph</a></li>
                                    </ul>
                                </nav>
                                <a href="#"><button>Admin</button></a>
                            </header>
                            {%app_entry%}
                            <footer>
                                {%config%}
                                {%scripts%}
                                {%renderer%}
                            </footer>
                        </body>
                    </html>'''
