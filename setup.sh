mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"adarsh.raj.2004@outlook.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
