def test_verify_the_functionality_of_the_new_registration_button(page):
    #jdi na stranku www.alza.cz
    page.goto('https://alza.cz/')

    #klikni v cookies na tlacitko "Rozumím"
    cookies_button = page.locator("a.btnx.cookies-info__button.js-cookies-info-accept")
    cookies_button.click()

    #klikni na odkaz "Moje Alza"
    moje_alza_button = page.locator("button[data-testid='headerContextMenuToggle']")
    moje_alza_button.click()

    #klikni na odkaz "Nová registrace"
    registration_link = page.locator("a.header-alz-65.header-alz-66.header-alz-71.header-alz-74.header-alz-162[href='https://www.alza.cz/Registration.htm'][title='Nová registrace']")
    registration_link.click()




def test_verification_of_the_functionality_of_the_search_field(page):
    #jdi na stranku www.alza.cz
    page.goto('https://alza.cz/')

    #klikni v cookies na tlačítko "Rozumím"
    cookies_button = page.locator("a.btnx.cookies-info__button.js-cookies-info-accept")
    cookies_button.click()

    #klikni do vyhledávacího pole
    search_input = page.locator("input[placeholder='Co hledáte? Např. kabel AlzaPower...']")
    search_input.click()

    #napiš "Kalhoty" do vyhledávacího pole
    search_input.fill("Kalhoty")

    #klikni na tlačítko Hledat
    search_button = page.locator("button[data-testid='button-search']")
    search_button.click()

    #počkej na načtení výsledků
    page.wait_for_load_state("networkidle")




def test_verification_of_the_functionality_of_the_left_link_panel_Zdravi_Bryle(page):
    #jdi na stranku www.alza.cz
    page.goto('https://alza.cz/')

    #klikni na cookies tlačítko "Rozumím"
    cookies_button = page.locator("a.btnx.cookies-info__button.js-cookies-info-accept")
    cookies_button.click()

    #v levem panelu klikni na odkaz "Zdraví"
    left_menu_item = page.locator("//li[@class='l0 leftMenuItem hm' and @id='litp18874562']")
    left_menu_item.click()

    #ve vyberu klikni na odkaz "Bryle"
    glasses_link = page.locator("a.catalogLocalTitlePage-alz-4 >> text=Brýle")
    glasses_link.click()






