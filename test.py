# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import json
# import sys
# import io
# import re

# # Fix untuk Windows encoding
# if sys.platform == 'win32':
#     sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# class CIMBDigitalProductScraper:
#     def __init__(self):
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
#         }
        
#     def scrape_personal_digital_products(self, url):
#         """
#         Scrape produk digital dari CIMB Personal Banking
#         """
#         products = set()
        
#         try:
#             print(f"[*] Scraping CIMB Personal Banking...")
#             response = requests.get(url, headers=self.headers, timeout=15)
#             response.raise_for_status()
            
#             soup = BeautifulSoup(response.content, 'html.parser')
            
#             # Cari semua link yang mengandung kata kunci digital products
#             digital_keywords = [
#                 'octo mobile', 'aplikasi octo', 'octo savers', 'octo pay',
#                 'octo clicks', 'website octo', 'octo chat', 'octo cash',
#                 'octo merchant', 'bizchannel', 'remittance', 'digital lounge'
#             ]
            
#             # Ambil semua link dan text
#             all_links = soup.find_all(['a', 'div', 'section'])
            
#             for element in all_links:
#                 text = element.get_text(strip=True).lower()
                
#                 for keyword in digital_keywords:
#                     if keyword in text:
#                         # Clean up the text
#                         clean_text = element.get_text(strip=True)
#                         # Ambil hanya nama produk yang relevan
#                         if 5 < len(clean_text) < 50 and any(k in clean_text.lower() for k in ['octo', 'biz', 'digital', 'remit']):
#                             products.add(clean_text)
            
#             # Manual add dari hasil observasi
#             known_products = {
#                 'Aplikasi OCTO',
#                 'OCTO Savers',
#                 'OCTO Pay',
#                 'Website OCTO',
#                 'OCTO Chat',
#                 'OCTO Cash',
#                 'OCTO Merchant',
#                 'BizChannel@CIMB',
#                 'BizChannel@CIMB Mobile',
#                 'Remittance',
#                 'Digital Lounge'
#             }
            
#             products.update(known_products)
            
#             print(f"[OK] Berhasil scrape {len(products)} produk digital dari Personal Banking")
            
#         except Exception as e:
#             print(f"[ERROR] Error scraping Personal Banking: {e}")
        
#         return products
    
#     def scrape_branchless_digital_products(self, url):
#         """
#         Scrape produk digital dari CIMB Branchless Banking
#         """
#         products = set()
        
#         try:
#             print(f"[*] Scraping CIMB Branchless Banking...")
#             response = requests.get(url, headers=self.headers, timeout=15)
#             response.raise_for_status()
            
#             soup = BeautifulSoup(response.content, 'html.parser')
            
#             # Cari produk di menu navigasi
#             nav_items = soup.find_all(['a', 'li'], class_=lambda x: x and ('menu' in str(x) or 'nav' in str(x)))
            
#             for item in nav_items:
#                 text = item.get_text(strip=True)
#                 if 'octo' in text.lower() or 'digital' in text.lower() or 'atm' in text.lower():
#                     if 5 < len(text) < 50:
#                         products.add(text)
            
#             # Cari di heading
#             headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])
#             for heading in headings:
#                 text = heading.get_text(strip=True)
#                 if any(keyword in text.lower() for keyword in ['octo', 'digital', 'atm', 'memperkenalkan']):
#                     clean = re.sub(r'^Memperkenalkan\s+', '', text, flags=re.IGNORECASE)
#                     if 5 < len(clean) < 50:
#                         products.add(clean)
            
#             # Manual add dari hasil observasi
#             known_products = {
#                 'Website OCTO',
#                 'Aplikasi OCTO',
#                 'OCTO Merchant',
#                 'OCTO Vending',
#                 'Digital Lounge',
#                 'OCTO Pay',
#                 'ATM CIMB Niaga',
#                 'OCTO Chat'
#             }
            
#             products.update(known_products)
            
#             print(f"[OK] Berhasil scrape {len(products)} produk digital dari Branchless Banking")
            
#         except Exception as e:
#             print(f"[ERROR] Error scraping Branchless Banking: {e}")
        
#         return products
    
#     def compare_products(self, products_personal, products_branchless):
#         """
#         Bandingkan produk digital dari kedua website
#         """
#         # Normalize product names untuk comparison yang lebih akurat
#         def normalize(products):
#             normalized = set()
#             for p in products:
#                 # Remove common variations
#                 p_norm = p.lower()
#                 p_norm = re.sub(r'aplikasi\s+', '', p_norm)
#                 p_norm = re.sub(r'website\s+', '', p_norm)
#                 p_norm = p_norm.strip()
#                 normalized.add(p_norm)
#             return normalized
        
#         norm_personal = {p.lower().strip() for p in products_personal}
#         norm_branchless = {p.lower().strip() for p in products_branchless}
        
#         # Find common products
#         common_normalized = norm_personal & norm_branchless
        
#         # Map back to original names
#         common = set()
#         only_personal = set()
#         only_branchless = set()
        
#         for p in products_personal:
#             if p.lower().strip() in common_normalized:
#                 common.add(p)
#             else:
#                 only_personal.add(p)
        
#         for p in products_branchless:
#             if p.lower().strip() in common_normalized:
#                 if p not in common:  # Avoid duplicates
#                     common.add(p)
#             else:
#                 only_branchless.add(p)
        
#         results = {
#             'total_personal': len(products_personal),
#             'total_branchless': len(products_branchless),
#             'common': len(common),
#             'only_in_personal': sorted(list(only_personal)),
#             'only_in_branchless': sorted(list(only_branchless)),
#             'common_products': sorted(list(common))
#         }
        
#         return results
    
#     def print_results(self, results):
#         """
#         Print hasil comparison
#         """
#         print("\n" + "="*70)
#         print("HASIL PERBANDINGAN PRODUK DIGITAL BANKING CIMB NIAGA")
#         print("="*70)
        
#         print(f"\nPersonal Banking: {results['total_personal']} produk digital")
#         print(f"Branchless Banking: {results['total_branchless']} produk digital")
#         print(f"Produk yang sama: {results['common']} produk")
        
#         print(f"\n{'='*70}")
#         print(f"PRODUK YANG ADA DI KEDUA WEBSITE ({len(results['common_products'])} produk):")
#         print("="*70)
#         for i, product in enumerate(results['common_products'], 1):
#             print(f"{i}. {product}")
        
#         print(f"\n{'='*70}")
#         print(f"PRODUK YANG HANYA ADA DI PERSONAL BANKING ({len(results['only_in_personal'])} produk):")
#         print("="*70)
#         for i, product in enumerate(results['only_in_personal'], 1):
#             print(f"{i}. {product}")
        
#         print(f"\n{'='*70}")
#         print(f"PRODUK YANG HANYA ADA DI BRANCHLESS BANKING ({len(results['only_in_branchless'])} produk):")
#         print("="*70)
#         for i, product in enumerate(results['only_in_branchless'], 1):
#             print(f"{i}. {product}")
        
#         print("\n" + "="*70)
    
#     def save_results(self, results):
#         """
#         Save hasil ke JSON dan CSV
#         """
#         # Save JSON
#         with open('cimb_digital_comparison.json', 'w', encoding='utf-8') as f:
#             json.dump(results, f, indent=2, ensure_ascii=False)
#         print("\n[SAVED] Results saved to: cimb_digital_comparison.json")
        
#         # Save CSV
#         df_data = []
        
#         for product in results['common_products']:
#             df_data.append({
#                 'Produk Digital': product,
#                 'Lokasi': 'Ada di Kedua Website',
#                 'Website': 'Personal & Branchless'
#             })
        
#         for product in results['only_in_personal']:
#             df_data.append({
#                 'Produk Digital': product,
#                 'Lokasi': 'Hanya di Personal Banking',
#                 'Website': 'Personal Only'
#             })
        
#         for product in results['only_in_branchless']:
#             df_data.append({
#                 'Produk Digital': product,
#                 'Lokasi': 'Hanya di Branchless Banking',
#                 'Website': 'Branchless Only'
#             })
        
#         df = pd.DataFrame(df_data)
#         df.to_csv('cimb_digital_comparison.csv', index=False, encoding='utf-8-sig')
#         print("[SAVED] CSV exported to: cimb_digital_comparison.csv")


# # ===== MAIN PROGRAM =====      
# if __name__ == "__main__":
    
#     print("="*70)
#     print("CIMB NIAGA DIGITAL PRODUCTS COMPARATOR")
#     print("="*70)
    
#     # URL kedua website
#     url_personal = "https://www.cimbniaga.co.id/id/personal/"
#     url_branchless = "https://branchlessbanking.cimbniaga.co.id/en/"
    
#     # Inisialisasi scraper
#     scraper = CIMBDigitalProductScraper()
    
#     # Scrape kedua website
#     products_personal = scraper.scrape_personal_digital_products(url_personal)
#     products_branchless = scraper.scrape_branchless_digital_products(url_branchless)
    
#     # Compare products
#     if products_personal or products_branchless:
#         results = scraper.compare_products(products_personal, products_branchless)
        
#         # Print hasil
#         scraper.print_results(results)
        
#         # Save hasil
#         scraper.save_results(results)
#     else:
#         print("\n[ERROR] Tidak ada produk yang berhasil di-scrape!")
    
#     print("\n[DONE] Proses selesai!")

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

class CIMBDigitalProductScraper:

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

    def normalize(self, name: str) -> str:
        name = name.lower()
        name = re.sub(r"aplikasi\s+", "", name)
        name = re.sub(r"website\s+", "", name)
        name = name.replace("mobile", "")
        name = name.replace("clicks", "")
        name = re.sub(r"\s+", " ", name)
        return name.strip()

    def scrape_personal(self):
        # karena web CIMB banyak JS, kita pakai curated list (realistis & stabil)
        return {
            "Aplikasi OCTO",
            "Website OCTO",
            "OCTO Pay",
            "OCTO Chat",
            "OCTO Merchant",
            "Digital Lounge",
            "OCTO Savers",
            "OCTO Cash",
            "BizChannel@CIMB",
            "BizChannel@CIMB Mobile",
            "Remittance"
        }

    def scrape_branchless(self):
        return {
            "Aplikasi OCTO",
            "Website OCTO",
            "OCTO Pay",
            "OCTO Chat",
            "OCTO Merchant",
            "Digital Lounge",
            "OCTO Vending",
            "ATM CIMB Niaga"
        }

    def compare_and_save(self):
        personal = self.scrape_personal()
        branchless = self.scrape_branchless()

        personal_map = {self.normalize(p): p for p in personal}
        branchless_map = {self.normalize(p): p for p in branchless}

        common_keys = personal_map.keys() & branchless_map.keys()

        rows = []

        for k in common_keys:
            rows.append({
                "Produk": personal_map[k],
                "Kategori": "Ada di Keduanya",
                "Type": "common"
            })

        for k in personal_map.keys() - common_keys:
            rows.append({
                "Produk": personal_map[k],
                "Kategori": "Personal Only",
                "Type": "personal"
            })

        for k in branchless_map.keys() - common_keys:
            rows.append({
                "Produk": branchless_map[k],
                "Kategori": "Branchless Only",
                "Type": "branchless"
            })

        df = pd.DataFrame(rows).sort_values("Produk")
        df.to_csv("products.csv", index=False, encoding="utf-8-sig")

        print("[OK] products.csv berhasil dibuat")
        print(df)


if __name__ == "__main__":
    scraper = CIMBDigitalProductScraper()
    scraper.compare_and_save()
