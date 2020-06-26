for file in conversion_todo/*.docx
 do
 	# for single file comment out the for do loop and uncomment the following line:
	#file="sample_docx/bhagavata_purana_-_canto_10_part_3_-_chapters_18-28_-_ten_commentaries.docx"
	mkdir unzipped
	cd unzipped
	unzip -q ../$file 	# this fails if the path contains a space!
	echo "### trying to convert $file"
	if grep -Fq 'Balaram' word/document.xml; #true;
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

			sed 's//fi/g'< word/comments.xml > word/_comments.xml
			sed 's//fl/g'< word/_comments.xml > word/comments.xml
			sed 's/ä/ā/g'< word/comments.xml > word/_comments.xml
			sed 's/é/ī/g'< word/_comments.xml > word/comments.xml
			sed 's/ü/ū/g'< word/comments.xml > word/_comments.xml
			sed 's/å/ṛ/g'< word/_comments.xml > word/comments.xml
			sed 's/è/ṝ/g'< word/comments.xml > word/_comments.xml
			sed 's/ì/ṅ/g'< word/_comments.xml > word/comments.xml
			sed 's/ñ/ṣ/g'< word/comments.xml > word/_comments.xml
			sed 's/ï/ñ/g'< word/_comments.xml > word/comments.xml
			sed 's/ö/ṭ/g'< word/comments.xml > word/_comments.xml
			sed 's/ò/ḍ/g'< word/_comments.xml > word/comments.xml
			sed 's/ë/ṇ/g'< word/comments.xml > word/_comments.xml
			sed 's/ç/ś/g'< word/_comments.xml > word/comments.xml
			sed 's/à/ṁ/g'< word/comments.xml > word/_comments.xml
			sed 's/ù/ḥ/g'< word/_comments.xml > word/comments.xml
			sed 's/ÿ/ḷ/g'< word/comments.xml > word/_comments.xml
			sed 's/û/ḹ/g'< word/_comments.xml > word/comments.xml
			sed 's/Ä/Ā/g'< word/comments.xml > word/_comments.xml
			sed 's/É/Ī/g'< word/_comments.xml > word/comments.xml
			sed 's/Ü/Ū/g'< word/comments.xml > word/_comments.xml
			sed 's/Å/Ṛ/g'< word/_comments.xml > word/comments.xml
			sed 's/È/Ṝ/g'< word/comments.xml > word/_comments.xml
			sed 's/Ì/Ṅ/g'< word/_comments.xml > word/comments.xml
			sed 's/Ñ/Ṣ/g'< word/comments.xml > word/_comments.xml
			sed 's/Ï/Ñ/g'< word/_comments.xml > word/comments.xml
			sed 's/Ö/Ṭ/g'< word/comments.xml > word/_comments.xml
			sed 's/Ò/Ḍ/g'< word/_comments.xml > word/comments.xml
			sed 's/Ë/Ṇ/g'< word/comments.xml > word/_comments.xml
			sed 's/Ç/Ś/g'< word/_comments.xml > word/comments.xml
			sed 's/À/Ṁ/g'< word/comments.xml > word/_comments.xml
			sed 's/Ù/Ḥ/g'< word/_comments.xml > word/comments.xml
			sed 's/ß/Ḷ/g'< word/comments.xml > word/_comments.xml

			sed 's//fi/g'< word/footer1.xml > word/_footer1.xml
			sed 's//fl/g'< word/_footer1.xml > word/footer1.xml
			sed 's/ä/ā/g'< word/footer1.xml > word/_footer1.xml
			sed 's/é/ī/g'< word/_footer1.xml > word/footer1.xml
			sed 's/ü/ū/g'< word/footer1.xml > word/_footer1.xml
			sed 's/å/ṛ/g'< word/_footer1.xml > word/footer1.xml
			sed 's/è/ṝ/g'< word/footer1.xml > word/_footer1.xml
			sed 's/ì/ṅ/g'< word/_footer1.xml > word/footer1.xml
			sed 's/ñ/ṣ/g'< word/footer1.xml > word/_footer1.xml
			sed 's/ï/ñ/g'< word/_footer1.xml > word/footer1.xml
			sed 's/ö/ṭ/g'< word/footer1.xml > word/_footer1.xml
			sed 's/ò/ḍ/g'< word/_footer1.xml > word/footer1.xml
			sed 's/ë/ṇ/g'< word/footer1.xml > word/_footer1.xml
			sed 's/ç/ś/g'< word/_footer1.xml > word/footer1.xml
			sed 's/à/ṁ/g'< word/footer1.xml > word/_footer1.xml
			sed 's/ù/ḥ/g'< word/_footer1.xml > word/footer1.xml
			sed 's/ÿ/ḷ/g'< word/footer1.xml > word/_footer1.xml
			sed 's/û/ḹ/g'< word/_footer1.xml > word/footer1.xml
			sed 's/Ä/Ā/g'< word/footer1.xml > word/_footer1.xml
			sed 's/É/Ī/g'< word/_footer1.xml > word/footer1.xml
			sed 's/Ü/Ū/g'< word/footer1.xml > word/_footer1.xml
			sed 's/Å/Ṛ/g'< word/_footer1.xml > word/footer1.xml
			sed 's/È/Ṝ/g'< word/footer1.xml > word/_footer1.xml
			sed 's/Ì/Ṅ/g'< word/_footer1.xml > word/footer1.xml
			sed 's/Ñ/Ṣ/g'< word/footer1.xml > word/_footer1.xml
			sed 's/Ï/Ñ/g'< word/_footer1.xml > word/footer1.xml
			sed 's/Ö/Ṭ/g'< word/footer1.xml > word/_footer1.xml
			sed 's/Ò/Ḍ/g'< word/_footer1.xml > word/footer1.xml
			sed 's/Ë/Ṇ/g'< word/footer1.xml > word/_footer1.xml
			sed 's/Ç/Ś/g'< word/_footer1.xml > word/footer1.xml
			sed 's/À/Ṁ/g'< word/footer1.xml > word/_footer1.xml
			sed 's/Ù/Ḥ/g'< word/_footer1.xml > word/footer1.xml
			sed 's/ß/Ḷ/g'< word/footer1.xml > word/_footer1.xml

			sed 's//fi/g'< word/footer2.xml > word/_footer2.xml
			sed 's//fl/g'< word/_footer2.xml > word/footer2.xml
			sed 's/ä/ā/g'< word/footer2.xml > word/_footer2.xml
			sed 's/é/ī/g'< word/_footer2.xml > word/footer2.xml
			sed 's/ü/ū/g'< word/footer2.xml > word/_footer2.xml
			sed 's/å/ṛ/g'< word/_footer2.xml > word/footer2.xml
			sed 's/è/ṝ/g'< word/footer2.xml > word/_footer2.xml
			sed 's/ì/ṅ/g'< word/_footer2.xml > word/footer2.xml
			sed 's/ñ/ṣ/g'< word/footer2.xml > word/_footer2.xml
			sed 's/ï/ñ/g'< word/_footer2.xml > word/footer2.xml
			sed 's/ö/ṭ/g'< word/footer2.xml > word/_footer2.xml
			sed 's/ò/ḍ/g'< word/_footer2.xml > word/footer2.xml
			sed 's/ë/ṇ/g'< word/footer2.xml > word/_footer2.xml
			sed 's/ç/ś/g'< word/_footer2.xml > word/footer2.xml
			sed 's/à/ṁ/g'< word/footer2.xml > word/_footer2.xml
			sed 's/ù/ḥ/g'< word/_footer2.xml > word/footer2.xml
			sed 's/ÿ/ḷ/g'< word/footer2.xml > word/_footer2.xml
			sed 's/û/ḹ/g'< word/_footer2.xml > word/footer2.xml
			sed 's/Ä/Ā/g'< word/footer2.xml > word/_footer2.xml
			sed 's/É/Ī/g'< word/_footer2.xml > word/footer2.xml
			sed 's/Ü/Ū/g'< word/footer2.xml > word/_footer2.xml
			sed 's/Å/Ṛ/g'< word/_footer2.xml > word/footer2.xml
			sed 's/È/Ṝ/g'< word/footer2.xml > word/_footer2.xml
			sed 's/Ì/Ṅ/g'< word/_footer2.xml > word/footer2.xml
			sed 's/Ñ/Ṣ/g'< word/footer2.xml > word/_footer2.xml
			sed 's/Ï/Ñ/g'< word/_footer2.xml > word/footer2.xml
			sed 's/Ö/Ṭ/g'< word/footer2.xml > word/_footer2.xml
			sed 's/Ò/Ḍ/g'< word/_footer2.xml > word/footer2.xml
			sed 's/Ë/Ṇ/g'< word/footer2.xml > word/_footer2.xml
			sed 's/Ç/Ś/g'< word/_footer2.xml > word/footer2.xml
			sed 's/À/Ṁ/g'< word/footer2.xml > word/_footer2.xml
			sed 's/Ù/Ḥ/g'< word/_footer2.xml > word/footer2.xml
			sed 's/ß/Ḷ/g'< word/footer2.xml > word/_footer2.xml

			sed 's//fi/g'< word/header1.xml > word/_header1.xml
			sed 's//fl/g'< word/_header1.xml > word/header1.xml
			sed 's/ä/ā/g'< word/header1.xml > word/_header1.xml
			sed 's/é/ī/g'< word/_header1.xml > word/header1.xml
			sed 's/ü/ū/g'< word/header1.xml > word/_header1.xml
			sed 's/å/ṛ/g'< word/_header1.xml > word/header1.xml
			sed 's/è/ṝ/g'< word/header1.xml > word/_header1.xml
			sed 's/ì/ṅ/g'< word/_header1.xml > word/header1.xml
			sed 's/ñ/ṣ/g'< word/header1.xml > word/_header1.xml
			sed 's/ï/ñ/g'< word/_header1.xml > word/header1.xml
			sed 's/ö/ṭ/g'< word/header1.xml > word/_header1.xml
			sed 's/ò/ḍ/g'< word/_header1.xml > word/header1.xml
			sed 's/ë/ṇ/g'< word/header1.xml > word/_header1.xml
			sed 's/ç/ś/g'< word/_header1.xml > word/header1.xml
			sed 's/à/ṁ/g'< word/header1.xml > word/_header1.xml
			sed 's/ù/ḥ/g'< word/_header1.xml > word/header1.xml
			sed 's/ÿ/ḷ/g'< word/header1.xml > word/_header1.xml
			sed 's/û/ḹ/g'< word/_header1.xml > word/header1.xml
			sed 's/Ä/Ā/g'< word/header1.xml > word/_header1.xml
			sed 's/É/Ī/g'< word/_header1.xml > word/header1.xml
			sed 's/Ü/Ū/g'< word/header1.xml > word/_header1.xml
			sed 's/Å/Ṛ/g'< word/_header1.xml > word/header1.xml
			sed 's/È/Ṝ/g'< word/header1.xml > word/_header1.xml
			sed 's/Ì/Ṅ/g'< word/_header1.xml > word/header1.xml
			sed 's/Ñ/Ṣ/g'< word/header1.xml > word/_header1.xml
			sed 's/Ï/Ñ/g'< word/_header1.xml > word/header1.xml
			sed 's/Ö/Ṭ/g'< word/header1.xml > word/_header1.xml
			sed 's/Ò/Ḍ/g'< word/_header1.xml > word/header1.xml
			sed 's/Ë/Ṇ/g'< word/header1.xml > word/_header1.xml
			sed 's/Ç/Ś/g'< word/_header1.xml > word/header1.xml
			sed 's/À/Ṁ/g'< word/header1.xml > word/_header1.xml
			sed 's/Ù/Ḥ/g'< word/_header1.xml > word/header1.xml
			sed 's/ß/Ḷ/g'< word/header1.xml > word/_header1.xml

			sed 's//fi/g'< word/header2.xml > word/_header2.xml
			sed 's//fl/g'< word/_header2.xml > word/header2.xml
			sed 's/ä/ā/g'< word/header2.xml > word/_header2.xml
			sed 's/é/ī/g'< word/_header2.xml > word/header2.xml
			sed 's/ü/ū/g'< word/header2.xml > word/_header2.xml
			sed 's/å/ṛ/g'< word/_header2.xml > word/header2.xml
			sed 's/è/ṝ/g'< word/header2.xml > word/_header2.xml
			sed 's/ì/ṅ/g'< word/_header2.xml > word/header2.xml
			sed 's/ñ/ṣ/g'< word/header2.xml > word/_header2.xml
			sed 's/ï/ñ/g'< word/_header2.xml > word/header2.xml
			sed 's/ö/ṭ/g'< word/header2.xml > word/_header2.xml
			sed 's/ò/ḍ/g'< word/_header2.xml > word/header2.xml
			sed 's/ë/ṇ/g'< word/header2.xml > word/_header2.xml
			sed 's/ç/ś/g'< word/_header2.xml > word/header2.xml
			sed 's/à/ṁ/g'< word/header2.xml > word/_header2.xml
			sed 's/ù/ḥ/g'< word/_header2.xml > word/header2.xml
			sed 's/ÿ/ḷ/g'< word/header2.xml > word/_header2.xml
			sed 's/û/ḹ/g'< word/_header2.xml > word/header2.xml
			sed 's/Ä/Ā/g'< word/header2.xml > word/_header2.xml
			sed 's/É/Ī/g'< word/_header2.xml > word/header2.xml
			sed 's/Ü/Ū/g'< word/header2.xml > word/_header2.xml
			sed 's/Å/Ṛ/g'< word/_header2.xml > word/header2.xml
			sed 's/È/Ṝ/g'< word/header2.xml > word/_header2.xml
			sed 's/Ì/Ṅ/g'< word/_header2.xml > word/header2.xml
			sed 's/Ñ/Ṣ/g'< word/header2.xml > word/_header2.xml
			sed 's/Ï/Ñ/g'< word/_header2.xml > word/header2.xml
			sed 's/Ö/Ṭ/g'< word/header2.xml > word/_header2.xml
			sed 's/Ò/Ḍ/g'< word/_header2.xml > word/header2.xml
			sed 's/Ë/Ṇ/g'< word/header2.xml > word/_header2.xml
			sed 's/Ç/Ś/g'< word/_header2.xml > word/header2.xml
			sed 's/À/Ṁ/g'< word/header2.xml > word/_header2.xml
			sed 's/Ù/Ḥ/g'< word/_header2.xml > word/header2.xml
			sed 's/ß/Ḷ/g'< word/header2.xml > word/_header2.xml

			# TODO: add candrabindu
			# sed 's/*/̐/g'< word/_document.xml > word/document.xml

			mv word/_document.xml word/document.xml

			sed 's/="Balaram"/="Times New Roman"/g' word/document.xml > word/_document.xml
			mv word/_document.xml word/document.xml

			sed 's/Balaram/Times New Roman/g' < word/styles.xml > word/_styles.xml
			mv word/_styles.xml word/styles.xml

			sed 's/Balaram/Times New Roman/g' < word/fontTable.xml > word/_fontTable.xml
			mv word/_fontTable.xml word/fontTable.xml

			sed 's/Balaram/Times New Roman/g'< word/endnotes.xml > word/_endnotes.xml
			mv word/_endnotes.xml word/endnotes.xml

			sed 's/Balaram/Times New Roman/g'< word/footnotes.xml > word/_footnotes.xml
			mv word/_footnotes.xml word/footnotes.xml

			sed 's/Balaram/Times New Roman/g'< word/comments.xml > word/_comments.xml
			mv word/_comments.xml word/comments.xml

			sed 's/Balaram/Times New Roman/g'< word/footer1.xml > word/_footer1.xml
			mv word/_footer1.xml word/footer1.xml

			sed 's/Balaram/Times New Roman/g'< word/footer2.xml > word/_footer2.xml
			mv word/_footer2.xml word/footer2.xml

			sed 's/Balaram/Times New Roman/g'< word/header1.xml > word/_header1.xml
			mv word/_header1.xml word/header1.xml

			sed 's/Balaram/Times New Roman/g'< word/header2.xml > word/_header2.xml
			mv word/_header2.xml word/header2.xml


			zip -rq ../$file *	# patch source docx file
			cd ..
			rm -rf unzipped/
			echo "### converted $file"
		else
			echo "## No Balaram found"
			cd ..
			rm -rf unzipped/
			continue
	fi
 done
