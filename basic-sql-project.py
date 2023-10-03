
# Bu projede SQLite veritabanını kullanarak bir adres defteri uygulaması oluşturacağız.
# Bu uygulama, kullanıcıların isimleri, telefon numaraları ve e-posta adresleri gibi kişisel bilgileri kaydedebileceği,
# bu bilgileri görüntüleyebileceği, güncelleyebileceği ve silebileceği bir adres defterini yönetmeye yönelik olacak.


# python'un SQLite veritabanını kullanabilmesi için gerekli olan modülü import ediyoruz.
import sqlite3

# veritabanımızı ve tabloyu oluşturuyoruz
def create_database():
    conn = sqlite3.connect("address_book.db")   # veritabanına bağlantı oluşturuyoruz.
    cursor = conn.cursor()  #veritabanı üzerinde işlem yapabilmek için bir "cursor" oluşturmanız gerekmektedir.

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
                   id INTEGER PRIMARY KEY,
                   first_name TEXT,
                   last_name TEXT,
                   phone_number TEXT,
                   email TEXT
        
        )
    ''')  ## SQL sorgusunu yürüt

    conn.commit()  # veritabanına değişiklikleri kaydet
    conn.close()   # veritabanı bağlantısını kapat



# kullanıcıdan yeni bir kişi eklemek için bilgileri alacak fonksiyonu yazalım:

def add_contact():
    first_name = input("İsim: ")
    last_name  = input("Soyisim: ")
    phone_number = input("Telefon Numarası: ")
    email = input("E-posta: ")

    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()

    cursor.execute('''
                   INSERT INTO contacts (first_name, last_name, phone_number, email)
                   VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, phone_number, email))

    conn.commit()
    conn.close()
    print("Kişi eklendi.")

# mevcut kişileri listelemesi için bir fonksiyon yazalımÇ

def list_contacts():
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()

    if not contacts:
        print("Adres defteri boş.")
    
    else:
        for contact in contacts:
            print(f"ID: {contact[0]}")
            print(f"İsim: {contact[1]} {contact[2]}")
            print(f"Telefon: {contact[3]}")
            print(f"E-posta: {contact[4]}")
            print("")

    conn.close()

# kullanıcıdan bir kişiyi silmek için bir fonksiyon yazalım:

def delete_contact():
    contact_id = input("Silmek istediğiniz kişinin ID'sini girin: ")

    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("Kişi bulunamadı.")
    else:
        print("Kişi silindi.")

    conn.close()

# kullanıcıfan bir seçenek seçmesini ve işlem yapmasını isteyen döngü

def main():
    create_database()

    while True:
        print("\nAdres Defteri Uygulaması")
        print("1. Kişi Ekle")
        print("2. Kişileri Lİstele")
        print("3. Kişi Sil")
        print("4. Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            list_contacts()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            print("Uygulama kapatılıyor.")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()


