generate_notebooks(){
rm -r public; mkdir public
for folder in $(ls challenges | egrep -i 'day_[0-9]*'); do
    echo "Generating notebooks in challenges/$folder";
    for notebook in $(ls challenges/$folder| egrep -i '.*.ipynb'); do
        echo "Found notebook  challenges/$folder/$notebook";
         jupyter nbconvert --execute --to html --output-dir="public/$folder" challenges/$folder/$notebook --HTMLExporter.theme=dark
    done
done
}


generate_index_html(){
     python generate_index.py
     cp -r assets public   
}

case $1 in
generate_notebooks)
generate_notebooks
;;
generate_index_html)
generate_index_html
;;
generate)
generate_notebooks
generate_index_html 
esac
