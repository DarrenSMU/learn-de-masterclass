awk '{gsub(/[0-9]{6-7}[A-Za-z]?/, "xxxxx", $NF);}1' generatedData.csv > replaced.csv
