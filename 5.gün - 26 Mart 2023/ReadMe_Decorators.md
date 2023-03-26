## **PyTtest Dekoratörler**

**@pytest.fixture**
> Bu dekoratör, testlerin ihtiyaç duyduğu önceden hazırlanmış verileri veya nesneleri sağlar. Fixture'lar, testler arasında paylaşılabilir ve her testin önceden belirlenmiş bir durumda çalışmasını sağlar.

**@pytest.mark.parametrize**
> Bu dekoratör, aynı test fonksiyonunun farklı parametrelerle tekrar tekrar çalıştırılmasını sağlar. Bu, testlerin daha modüler ve ölçeklenebilir hale gelmesine olanak tanır.

**@pytest.mark.skip**
> Bu dekoratör, belirtilen testleri atlamak için kullanılır. Bu, testlerde hatalar varsa veya bazı testlerin sadece belirli durumlarda çalışması gerektiğinde faydalıdır.

**@pytest.mark.xfail**
> Bu dekoratör, belirtilen testlerin başarısız olması bekleniyor olsa bile, hala çalıştırılmasını sağlar. Bu, hataları tespit etmek ve gelecekteki hata düzeltmelerini planlamak için yararlı olabilir.

**@pytest.mark.timeout**
> Bu dekoratör, testlerin belirli bir süre içinde tamamlanmasını zorlar. Bu, testlerin sonsuz döngüye girme veya diğer performans sorunlarına neden olabilecek hataları yakalamak için kullanılabilir.

**@pytest.mark.flaky**
> Bu dekoratör, belirtilen testlerin bazen başarısız olabileceğini işaret eder. Bu, testlerin zaman zaman çevresel faktörlerden etkilenmesi durumunda faydalı olabilir.

