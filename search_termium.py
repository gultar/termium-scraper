import asyncio
from playwright.async_api import async_playwright


async def search_termium(query):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.btb.termiumplus.gc.ca/tpv2alpha/alpha-fra.html?lang=fra")
        
        # Type the query into the search input field
        await page.type("#searchfield", query)

        # Click the search button
        await page.click("#comencsrch")
        await page.wait_for_selector('section.recordSet')

        # Extract information from each search result or return an empty array if no results are found
        results = await page.evaluate('''() => {
            
            const resultItems = document.querySelectorAll('.panel-body.mrgn-bttm-sm.mrgn-tp-sm');

            const resultData = [];

            resultItems.forEach((item) => {
                const entry = {
                    english:{
                        subject:"",
                        term:"",
                        context:""
                    },
                    francais:{
                        domaine:"",
                        terme:"",
                        contexte:""
                    }
                };

                // Extract English, French, and Spanish records
                const records = item.querySelectorAll('.col-md-4');
                records.forEach((record, index) => {
                    try{
                        if(index == 0){
                            //English Record
                            const subjectFieldElements = record.querySelector('.panel-body ul li');
                            entry.english.subject = subjectFieldElements.innerText
            
                            const keyTermsElements = record.querySelectorAll(`.list-unstyled .text-primary`);
                            const secondaryTermsElement = record.querySelector(`.list-unstyled .text-primary mark`);
                            
                            keyTermsElements.forEach(el =>{
                                entry.english.term +=  el.innerText +"\n\n"
                            })
            
                            const context = record.querySelector('.panel-body div.wb-init p')
                            entry.english.context = context.innerText
                            
                        } else if(index == 1){
                            //English Record
                            const subjectFieldElements = record.querySelector('.panel-body ul li');
                            entry.francais.domaine = subjectFieldElements.innerText
            
                            const keyTermsElements = record.querySelectorAll(`.list-unstyled .text-primary`);

                            keyTermsElements.forEach(el =>{
                                entry.francais.terme += el.innerText + "\n\n"
                            })
                                            
                            const context = record.querySelector('.panel-body div.wb-init p')
                            entry.francais.contexte = context.innerText
                        } 
                    }catch(e){
                        console.log(e)
                    }

                });
                resultData.push(entry);
            })
            return resultData
        }''')

        # Close the browser
        await browser.close()
        return results

# async def main():

#     # add in other UI elements here e.g. title, input data etc
#     query_string = "business"
#     # results = await search_vitrinelinguistique(query_string)
#     results = await search_termium(query_string)
#     # print(results)
#     st.write(results)
 

# if __name__ == '__main__':
#     loop = asyncio.ProactorEventLoop()
#     loop.run_until_complete(main())

