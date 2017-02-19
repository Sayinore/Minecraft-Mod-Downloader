#v1.0.5
2017-2-19  
- Fixed bugs
    - Cannot check if the link in the invalid download links, like `请看楼下.com`
    - Cannot install dragged mod file, because of str with two quotation marks, like `"'C:\A\Path\For\Example'"`
- Changed
    - Str with var like `"You are " + str(age) + " years old!"` --> `"You are %d years old!" % age`
- Added
    - Chinese translation

#v1.0.0
2017-2-18