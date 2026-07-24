https://github.com/quarto-dev/quarto-cli/releases/download/v1.9.38/quarto-1.9.38-linux-amd64.deb

wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.9.38/quarto-1.9.38-linux-amd64.deb

sudo apt install ./quarto-1.9.38-linux-amd64.deb

Verify the version 👍
quarto --version

Check dependencies:
quarto check
Install the non installed dependency, e.g. for r markdown
Rscript -e 'install.packages("rmarkdown", repos="https://cloud.r-project.org")' 
sudo apt install chromium-browser
quarto install tinytex
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb


# Automatic Github action, from 

kworou.github.io/.github/workflows