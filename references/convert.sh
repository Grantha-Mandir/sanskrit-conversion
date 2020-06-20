for file in conversion_todo/*.docx
 do
 	# for single file comment out the for do loop and uncomment the following line:
	#file="sample_docx/bhagavata_purana_-_canto_10_part_3_-_chapters_18-28_-_ten_commentaries.docx"
	mkdir unzipped
	cd unzipped
	unzip -q ../$file 	# this fails if the path contains a space!
	echo "### trying to convert $file"
	if grep -Fq 'Balaram' word/document.xml;
		then
			echo "## Balaram found"
			sed 's//fi/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's//fl/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/ä/ā/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/é/ī/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/ü/ū/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/å/ṛ/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/è/ṝ/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/ì/ṅ/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/ñ/ṣ/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/ï/ñ/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/ö/ṭ/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/ò/ḍ/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/ë/ṇ/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/ç/ś/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/à/ṁ/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/ù/ḥ/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/ÿ/ḷ/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/û/ḹ/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/Ä/Ā/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/É/Ī/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/Ü/Ū/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/Å/Ṛ/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/È/Ṝ/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/Ì/Ṅ/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/Ñ/Ṣ/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/Ï/Ñ/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/Ö/Ṭ/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/Ò/Ḍ/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/Ë/Ṇ/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/Ç/Ś/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/À/Ṁ/g'< word/footnotes.xml > word/_footnotes.xml
			sed 's/Ù/Ḥ/g'< word/_footnotes.xml > word/footnotes.xml
			sed 's/ß/Ḷ/g'< word/footnotes.xml > word/_footnotes.xml
			mv word/_footnotes.xml word/footnotes.xml

			sed 's//fi/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's//fl/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/ä/ā/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/é/ī/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/ü/ū/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/å/ṛ/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/è/ṝ/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/ì/ṅ/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/ñ/ṣ/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/ï/ñ/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/ö/ṭ/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/ò/ḍ/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/ë/ṇ/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/ç/ś/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/à/ṁ/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/ù/ḥ/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/ÿ/ḷ/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/û/ḹ/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/Ä/Ā/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/É/Ī/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/Ü/Ū/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/Å/Ṛ/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/È/Ṝ/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/Ì/Ṅ/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/Ñ/Ṣ/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/Ï/Ñ/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/Ö/Ṭ/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/Ò/Ḍ/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/Ë/Ṇ/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/Ç/Ś/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/À/Ṁ/g'< word/endnotes.xml > word/_endnotes.xml
			sed 's/Ù/Ḥ/g'< word/_endnotes.xml > word/endnotes.xml
			sed 's/ß/Ḷ/g'< word/endnotes.xml > word/_endnotes.xml
			mv word/_endnotes.xml word/endnotes.xml

			sed 's//fi/g'< word/document.xml > word/_document.xml
			sed 's//fl/g'< word/_document.xml > word/document.xml
			sed 's/ä/ā/g'< word/document.xml > word/_document.xml
			sed 's/é/ī/g'< word/_document.xml > word/document.xml
			sed 's/ü/ū/g'< word/document.xml > word/_document.xml
			sed 's/å/ṛ/g'< word/_document.xml > word/document.xml
			sed 's/è/ṝ/g'< word/document.xml > word/_document.xml
			sed 's/ì/ṅ/g'< word/_document.xml > word/document.xml
			sed 's/ñ/ṣ/g'< word/document.xml > word/_document.xml
			sed 's/ï/ñ/g'< word/_document.xml > word/document.xml
			sed 's/ö/ṭ/g'< word/document.xml > word/_document.xml
			sed 's/ò/ḍ/g'< word/_document.xml > word/document.xml
			sed 's/ë/ṇ/g'< word/document.xml > word/_document.xml
			sed 's/ç/ś/g'< word/_document.xml > word/document.xml
			sed 's/à/ṁ/g'< word/document.xml > word/_document.xml
			sed 's/ù/ḥ/g'< word/_document.xml > word/document.xml
			sed 's/ÿ/ḷ/g'< word/document.xml > word/_document.xml
			sed 's/û/ḹ/g'< word/_document.xml > word/document.xml
			sed 's/Ä/Ā/g'< word/document.xml > word/_document.xml
			sed 's/É/Ī/g'< word/_document.xml > word/document.xml
			sed 's/Ü/Ū/g'< word/document.xml > word/_document.xml
			sed 's/Å/Ṛ/g'< word/_document.xml > word/document.xml
			sed 's/È/Ṝ/g'< word/document.xml > word/_document.xml
			sed 's/Ì/Ṅ/g'< word/_document.xml > word/document.xml
			sed 's/Ñ/Ṣ/g'< word/document.xml > word/_document.xml
			sed 's/Ï/Ñ/g'< word/_document.xml > word/document.xml
			sed 's/Ö/Ṭ/g'< word/document.xml > word/_document.xml
			sed 's/Ò/Ḍ/g'< word/_document.xml > word/document.xml
			sed 's/Ë/Ṇ/g'< word/document.xml > word/_document.xml
			sed 's/Ç/Ś/g'< word/_document.xml > word/document.xml
			sed 's/À/Ṁ/g'< word/document.xml > word/_document.xml
			sed 's/Ù/Ḥ/g'< word/_document.xml > word/document.xml
			sed 's/ß/Ḷ/g'< word/document.xml > word/_document.xml

			# TODO: add candrabindu
			# sed 's/*/̐/g'< word/_document.xml > word/document.xml

			# TODO: process docx header, as seen in
			# bhagavata_purana_-_canto_10_part_3_-_chapters 18-28_-_ten_commentaries.docx
			mv word/_document.xml word/document.xml

			sed 's/="Balaram"/="Times New Roman"/g' word/document.xml > word/_document.xml
			mv word/_document.xml word/document.xml

			sed 's/Balaram/Times New Roman/g' < word/styles.xml > word/_styles.xml
			mv word/_styles.xml word/styles.xml

			sed 's/Balaram/Times New Roman/g' < word/fontTable.xml > word/_fontTable.xml
			mv word/_fontTable.xml word/fontTable.xml
			zip -rq ../$file *	# patch source docx file
			echo "### converted $file"
			cd ..
			rm -rf unzipped/
		else
			echo "## No Balaram found"
			cd ..
			rm -rf unzipped/
			continue
	fi
 done
