mkdir -p ~/.streamlit/

echo"\
[server]\n\
port = $PORT\n\
enableCROS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml