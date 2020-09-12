# Belajar keyword argument list
# memasukkan argument dengan menyebutkan argument atau nama parameternya.
# selanjutnya akan dicombine menjadi sebuah dictionary

def create_html(tag, text, **attr): # menggunakan double star (**), dan akan menghasilkan tipe data dictionary
    html = f"<{tag}"

    for key, value in attr.items(): # mengeluarkan keyword argument sama dengan mengeluarkan dictionary
        html += f" {key}='{value}' " 

    html += f"> {text} </{tag}>"
    return html

html = create_html("p", "Hello Python")
print(html)

html = create_html("a", "Ini link", href="www.facebook.com")
print(html)
