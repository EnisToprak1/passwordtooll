import re
import requests
import random


def display_banner():
    banner = """
 #####      ##      ####     ####    ##   ##   ####    #####    ####
 ##  ##    ####    ##  ##   ##  ##   ##   ##  ##  ##   ##  ##   ## ##
 ##  ##   ##  ##   ##       ##       ##   ##  ##  ##   ##  ##   ##  ##
 #####    ######    ####     ####    ## # ##  ##  ##   #####    ##  ##
 ##       ##  ##       ##       ##   #######  ##  ##   ####     ##  ##
 ##       ##  ##   ##  ##   ##  ##   ### ###  ##  ##   ## ##    ## ##
 ##       ##  ##    ####     ####    ##   ##   ####    ##  ##   ####
    """
    print(banner)


default_language = "en"# Varsayılan dil (İngilizce)


supported_languages = {# Tüm desteklenen diller
    "en": "English",
    "tr": "Türkçe",
    "fr": "Français",
    "es": "Español",
    "de": "Deutsch",
    "zh": "中文",
    "ru": "Русский",
    "ar": "العربية",
    "hi": "हिन्दी",
    "ja": "日本語",
    # Daha fazla dil ekleyebilirsiniz...
}


TRANSLATE_API_URL = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={lang}&dt=t&q={text}" # Google Translate API endpoint ve key


messages = { # Mesajların İngilizce karşılıkları
    "enter_password": "Enter your password: ",
    "password_analysis": "Password Analysis",
    "strength_level": "Strength Level",
    "suggestions": "Suggestions",
    "extra_suggestions": "Extra Suggestions to Strengthen Your Password",
    "congratulations": "Congratulations! Your password is strong enough.",
    "try_again": "Please strengthen your password and try again!",
    "usage": "Usage: python sifre_kontrol.py",
    "example_usage": "Example usage: python sifre_kontrol.py",
    "weak": "Weak",
    "moderate": "Moderate",
    "strong": "Strong",
    "very_strong": "Very Strong",
    "criteria": {
        "length": "Your password should be at least 12 characters long!",
        "uppercase": "Add at least one uppercase letter to your password!",
        "lowercase": "Add at least one lowercase letter to your password!",
        "number": "Add at least one number to your password!",
        "special_character": "Add at least one special character to your password!"
    }
}


extra_suggestions = [ # Ekstra öneriler
    "Use a mix of uppercase and lowercase letters.",
    "Include numbers and special characters in your password.",
    "Avoid using common words or easily guessable information.",
    "Make your password at least 16 characters long.",
    "Consider using a passphrase made of random words.",
    "Don't reuse passwords from other accounts.",
    "Avoid sequential patterns like '12345' or 'abcdef'."
]


def translate_message(message, lang):# Çeviri fonksiyonu
    try:
        if lang == "en":  # Eğer dil İngilizce ise çeviri gerekmez
            return message
        response = requests.get(TRANSLATE_API_URL.format(lang=lang, text=message))
        if response.status_code == 200:
            translated_text = response.json()[0][0][0]
            return translated_text
    except Exception as e:
        print(f"Translation error: {e}")
    return message  # Hata durumunda orijinal mesajı döndür


def password_check(password, lang):# Şifre kontrol fonksiyonu
    score = 0
    max_score = 5
    suggestions = []

    
    if len(password) >= 12:# Uzunluk kontrolü
        score += 1
    else:
        suggestions.append(translate_message(messages["criteria"]["length"], lang))

   
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append(translate_message(messages["criteria"]["uppercase"], lang))

   
    if re.search(r"[a-z]", password): # Küçük harf kontrolü
        score += 1
    else:
        suggestions.append(translate_message(messages["criteria"]["lowercase"], lang))

    
    if re.search(r"[0-9]", password):# Sayı kontrolü
        score += 1
    else:
        suggestions.append(translate_message(messages["criteria"]["number"], lang))

  
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # Özel karakter kontrolü
        score += 1
    else:
        suggestions.append(translate_message(messages["criteria"]["special_character"], lang))

    
    percentage = (score / max_score) * 100 # Güç seviyesi ve yüzde
    if percentage == 100:
        strength = translate_message(messages["very_strong"], lang)
    elif percentage >= 80:
        strength = translate_message(messages["strong"], lang)
    elif percentage >= 50:
        strength = translate_message(messages["moderate"], lang)
    else:
        strength = translate_message(messages["weak"], lang)

    return strength, percentage, suggestions


display_banner() # Program başladığında ASCII sanatını göster


print("Supported languages:")# Dil seçimi
for code, name in supported_languages.items():
    print(f"- {code}: {name}")

while True:
    selected_language = input("Please select a language (e.g., en, tr, fr): ").strip().lower()
    if selected_language in supported_languages:
        break
    else:
        print("Invalid language selection. Please try again.")


print(translate_message(messages["usage"], selected_language))# Kullanıcı döngüsü
print(translate_message(messages["example_usage"], selected_language))

while True:
    user_password = input(translate_message(messages["enter_password"], selected_language))
    strength, percentage, suggestions = password_check(user_password, selected_language)

    print(f"\n{translate_message(messages['password_analysis'], selected_language)}:")
    print(f"{translate_message(messages['strength_level'], selected_language)}: {strength} ({percentage:.0f}%)")

    if suggestions:
        print(f"\n{translate_message(messages['suggestions'], selected_language)}:")
        for suggestion in suggestions:
            print(f"- {suggestion}")

    if percentage < 80:  
        print(f"\n{translate_message(messages['extra_suggestions'], selected_language)}:") # Ekstra öneriler ekle
        for extra_suggestion in random.sample(extra_suggestions, 3):
            print(f"- {translate_message(extra_suggestion, selected_language)}")

    if strength == translate_message(messages["very_strong"], selected_language) or strength == translate_message(messages["strong"], selected_language):
        print(f"\n{translate_message(messages['congratulations'], selected_language)}")
        break
    else:
        print(f"\n{translate_message(messages['try_again'], selected_language)}")
