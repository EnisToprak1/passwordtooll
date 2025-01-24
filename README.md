# passwordtooll
Ad-Soyad: Salih Sefa Korkmaz Numara:2320191019 // Ad-Soyad: Enis Seha Toprak Numara:2320191038


Kurulum
Bu kılavuz, Şifre Güvenliği Analizi Aracı'nı bilgisayarınıza yüklemeniz ve çalıştırmanız için gereken adımları açıklar.

Kurulum
### Kurulum

Bu kılavuz, Şifre Güvenliği Analizi Aracı'nı bilgisayarınıza yüklemeniz ve çalıştırmanız için gereken adımları açıklar.

---

#### 1. Python Kurulu mu Kontrol Edin

Öncelikle bilgisayarınızda Python'un kurulu olup olmadığını kontrol etmeniz gerekir. Aşağıdaki adımları izleyin:

- Komut satırını (Windows için `cmd`, macOS/Linux için `Terminal`) açın.
- Aşağıdaki komutu yazın ve `Enter` tuşuna basın:

  ```
  python --version
  ```

  veya

  ```
  python3 --version
  ```

- Eğer Python'un versiyon bilgisi görüntüleniyorsa, Python kurulu demektir. Aksi takdirde, Python'u indirip yüklemeniz gerekecek.

---

#### 2. Python İndirme ve Yükleme

Eğer bilgisayarınızda Python yüklü değilse, aşağıdaki adımları izleyerek yükleyebilirsiniz:

1. [Python'un resmi web sitesini](https://www.python.org/downloads/) ziyaret edin.
2. İşletim sisteminize uygun olan Python sürümünü indirin (genellikle en son sürüm önerilir).
3. İndirme tamamlandıktan sonra, kurulum dosyasını çalıştırın.
4. **Kurulum sırasında "Add Python to PATH" seçeneğini işaretlemeyi unutmayın.**

Kurulum tamamlandıktan sonra, tekrar komut satırında aşağıdaki komutlardan biriyle Python kurulumunu kontrol edebilirsiniz:

  ```
  python --version
  ```

  veya

  ```
  python3 --version
  ```

---

#### 3. GitHub Deposu

Şifre Güvenliği Analizi Aracı'nın kaynak koduna GitHub üzerinden erişebilirsiniz. Depoyu klonlamak için şu adımları izleyin:

- Komut satırını açın ve aşağıdaki komutu çalıştırın:

  ```
  git clone https://github.com/kullanici_adi/sifre-guvenlik-araci.git
  ```

  **Not:** Depo URL'sini projeniz için uygun olan GitHub bağlantısıyla değiştirin.

- Depo başarıyla klonlandıktan sonra, proje klasörünü geçmek için şu komutu kullanın:

  ```
  cd sifre-guvenlik-araci
  ```

---

#### 4. Gerekli Kütüphaneleri Yükleme

Projede kullanılan herhangi bir Python kütüphanesi varsa, bunları yüklemek için aşağıdaki komutu çalıştırın:

  ```
  pip install -r requirements.txt
  ```

---

#### 5. Aracı Çalıştırma

Kurulum tamamlandıktan sonra, aracı çalıştırmak için şu adımı uygulayın:

  ```
  python sifre_guvenlik_araci.py
  ```

  veya

  ```
  python3 sifre_guvenlik_araci.py
  ```

Eğer uygulama kullanıcı dostu bir arayüze sahipse, bu komut çalıştırıldığında arayüz otomatik olarak açılacaktır.

---

Artık Şifre Güvenliği Analizi Aracı'nı başarıyla kurup çalıştırmış olmalısınız. 🎉
