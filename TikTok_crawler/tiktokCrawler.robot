*** Settings ***
Library  SeleniumLibrary
Library  ..\\Libraries\\manageCSV.py




Suite Setup  Open Browser   ${STARTSEITE}  edge
#Suite Teardown  Close Browser
*** Variables ***
${STARTSEITE}                                   https://www.tiktok.com/@vivian_radtke
${XPATH_ERSTES_VIDEO}                           //*[@id="main-content-others_homepage"]/div/div[2]/div[3]/div/div[1]/div
${XPATH_NAECHSTES_VIDEO}                        //*[@id="immersive-player"]/div[2]/div[2]/button
${XPATH_BESCHREIBUNG}                           //*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]
${HERR_GOETZ}                                   Herr Götz
${ANZAHL_POSTS}                                 500
${TESTANZAHL}                                   50
*** Test Cases ***
Crawler

    Sleep  15s
    Click Element                              ${XPATH_ERSTES_VIDEO}
    ${IST_HERR_GOETZ}  Run Keyword And Return Status  Element Should Contain  ${XPATH_BESCHREIBUNG}  ${HERR_GOETZ}

    FOR  ${INDEX}  IN RANGE  1   ${ANZAHL_POSTS}
        ${IST_HERR_GOETZ}  Run Keyword And Return Status  Element Should Contain  ${XPATH_BESCHREIBUNG}  ${HERR_GOETZ}
        IF  ${IST_HERR_GOETZ} == True
            Log To Console                             Herr Götz gefunden
            Sleep  1s

            ${VIDEO_URL}                               Get Location
            Log   ${VIDEO_URL}
            Schreibe CSV                               ${VIDEO_URL}
            Press Keys                                 None  ARROW_DOWN

        ELSE

            sleep  1s

            Press Keys                                 None  ARROW_DOWN

        END
    END
    Sleep  5s





*** Keywords ***

