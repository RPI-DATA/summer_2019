mkdir temp_grade
#Step 1: Convert all notebooks to .py files
jupyter nbconvert --output-dir='./temp_grade'  --to script '*.ipynb'   

#Step 2: Copy the appropriate .OK and tests to temp diretory. 


#Step 3 Append


FILES= .temp_grade/*
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  cat $f notebook_append.py >> $f
  #execute the file
  
done
