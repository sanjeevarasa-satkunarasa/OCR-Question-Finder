import os
from bs4 import BeautifulSoup

# Define the subject variable
subject = "Kjemi_2"  # You can change this to any subject you want

html_content = """
<<li>
          <h3>V2024</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/Eksamen REA3046 Kjemi 2 vår 24.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Mangler</p>
        </li>
        <li>
          <h3>H2023 LK20</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3046 Eksamen H23.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="/Løsningsforslag/Veiledning Finne Aunivers Løsningsforslag til Eksamensoppgaver PDF.pdf"
            target="_blank" download>
            Ligger på Aunivers</a>
        </li>
        <li>
          <h3>V2023 LK20</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3046 Eksamen V23.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="/Løsningsforslag/Veiledning Finne Aunivers Løsningsforslag til Eksamensoppgaver PDF.pdf"
            target="_blank" download>
            Ligger på Aunivers</a>
        </li>
        <li>
          <h3>Eksempel V2023</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/Eksempeloppgave V2023 REA3046 Eksamen Skriftlig.pdf" target="_blank"
            download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2022</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012_Kjemi2_H22 endret nov.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="/Løsningsforslag/Veiledning Finne Aunivers Løsningsforslag til Eksamensoppgaver PDF.pdf"
            target="_blank" download>
            Ligger på Aunivers</a>
        </li>
        <li>
          <h3>V2022</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/V22.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="/Løsningsforslag/Veiledning Finne Aunivers Løsningsforslag til Eksamensoppgaver PDF.pdf"
            target="_blank" download>
            Ligger på Aunivers</a>
        </li>
        <li>
          <h3>H2021</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012_Kjemi2 H21.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <h3>V2021</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012 Kjemi2 V21.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="/Løsningsforslag/Veiledning Finne Aunivers Løsningsforslag til Eksamensoppgaver PDF.pdf"
            target="_blank" download>
            Ligger på Aunivers</a>
        </li>
        <li>
          <h3>H2020</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012 Kjemi2 H20.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="/Løsningsforslag/Veiledning Finne Aunivers Løsningsforslag til Eksamensoppgaver PDF.pdf"
            target="_blank" download>
            Ligger på Aunivers</a>
        </li>
        <li>
          <h3>V2020</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/rea3012_kjemi2 v20.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="/Løsningsforslag/Veiledning Finne Aunivers Løsningsforslag til Eksamensoppgaver PDF.pdf"
            target="_blank" download>
            Ligger på Aunivers</a>
        </li>
        <li>
          <h3>H2019</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012_Kjemi2 H19.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2019</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012-Kjemi2-V19.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2018</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012_Kjemi2 H18.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2018</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012_Kjemi2 V18.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2017</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver//Kjemi 2/kjemi2_17H.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2017</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/kjemi2_17V.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="https://delmatte.no/kjemi/kjemi2_17V_LF.pdf" target="_blank" download>
            Løsning
          </a>
        </li>
        <li>
          <h3>H2016</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/kjemi2_16H.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2016</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/kjemi2_16V.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2015</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/kjemi 2/kjemi2_15v.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2015</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/kjemi2_15H.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="https://delmatte.no/kjemi/kjemi2_15V_LF.pdf" target="_blank" download>
            Løsning
          </a>
        </li>
        <li>
          <h3>H2014</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver//Kjemi 2/kjemi2_14H.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2014</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/kjemi2_14V.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2013</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012_Kjemi2 H13.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2013</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012_Kjemi2 V13.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="/Løsningsforslag/kjemi 2/Vår 2013 Løsninger.pdf" target="_blank" download>
            Løsning
          </a>
        </li>
        <li>
          <h3>H2012</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012_Kjemi2 H12.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="/Løsningsforslag/kjemi 2/Høst 2012 Løsninger.pdf" target="_blank" download>
            Løsning
          </a>
        </li>
        <li>
          <h3>V2012</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver//Kjemi 2/REA3012_Kjemi2 V12.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="/Løsningsforslag/kjemi 2/VaÌŠr 2012 Løsninger.pdf" target="_blank" download>
            Løsning</a>
        </li>
        <li>
          <h3>H2011</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012_Kjemi2 H11.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <a href="/Løsningsforslag/kjemi 2/Høst 2011 Løsninger.pdf" target="_blank" download>
            Løsning
          </a>
        </li>
        <li>
          <h3>V2011</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/REA3012_Kjemi2 V11.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2010</h3>
        </li>
        <li>
          <p>Oppgave (Mangler)</p>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2010</h3>
        </li>
        <li>
          <p>Oppgave (Mangler)</p>
        </li>
        <li>
          <a href="/Løsningsforslag/kjemi 2/Kjemi 2_Vr 2010_Lsningsforslag.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <h3>H2009</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver//Kjemi 2/2009H_AA6249_Kjemi_3KJ_privatister.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2009</h3>
        </li>
        <li>
          <p>Oppgave (Mangler)</p>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2008</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2008H_Kjemi_3KJ_AA6247_6249.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2008</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2008_Kjemi_3KJ_AA6247.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2008 Privatister</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2008_Kjemi_3KJ_AA6249_privatister.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2007</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2007H_Kjemi_3KJ_AA6247_6249.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2007</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2007_Kjemi_3KJ_AA6247.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2006</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2006H_Kjemi_3KJ_AA6247_AA6249.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2006</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2006_Kjemi_3KJ_AA6247.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2005</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2005H_Kjemi_3KJ_AA6247_AA6249.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2005</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/V2005_Kjemi_3KJ_AA6247_6249.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2004</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2004H_Kjemi_3KJ_AA6247_AA6249.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2004</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2004_Kjemi_3KJ_AA6247_AA6249.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2003</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2003H_Kjemi_3KJ_AA6247.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2003</h3>
        </li>
        <li>
          <p>Oppgave (Mangler)</p>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2005</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2005H_Kjemi_3KJ_AA6247_AA6249.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2005</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/V2005_Kjemi_3KJ_AA6247_6249.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2004</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2004H_Kjemi_3KJ_AA6247_AA6249.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2004</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2004_Kjemi_3KJ_AA6247_AA6249.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2003</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2003H_Kjemi_3KJ_AA6247.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2003</h3>
        </li>
        <li>
          <p>Oppgave (Mangler)</p>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2002</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2002H_Kjemi_3KJ_AA6247.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2002</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2002_Kjemi_3KJ_AA6247.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2001</h3>
        </li>
        <li>
          <p>Oppgave (Mangler)</p>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2001</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2001_Kjemi_3KJ_AA6247.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H2000</h3>
        </li>
        <li>
          <p>Oppgave (Mangler)</p>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V2000</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/2000_Kjemi_3KJ_AA6247.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1999</h3>
        </li>
        <li>
          <p>Oppgave (Mangler)</p>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1999</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1999_Kjemi_3KJ_AA6247.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1998</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1998H_Kjemi_3KJ_AA6240_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1998</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1998_Kjemi_3KJ_AA6240_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1997</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1997H_Kjemi_3KJ_AA6240_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1997</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1997_Kjemi_3KJ_AA6240_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1996</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1996H_Kjemi_3KJ_AF3361BM.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1996</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1996_Kjemi_3KJ_AF3361.pdf" target="_blank" download>
            Oppgave
          </a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1995</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1995H_Kjemi_3KJ_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1995</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1995_Kjemi_3KJ_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1994</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1994H_Kjemi_3KJ_AF3361BM.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1994</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1994_Kjemi_3KJ_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1993</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1993H_Kjemi_3KJ_AF3361BM.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1993</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1993_Kjemi_3KJ_AF3361BM.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1992</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1992H_Kjemi_3KJ_AF3361BM.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1992</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1992_Kjemi_3KJ_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1991</h3>
        </li>
        <li>
          <p>Oppgave (Mangler)</p>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1991</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1991_Kjemi_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1990</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1990H_Kjemi_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1990</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1990_Kjemi_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1989</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1989H_Kjemi_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1989</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1989_Kjemi_AF3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1998</h3>
        </li>
        <li>
          <p>Oppgave (Mangler)</p>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1988</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1988_Kjemi_AF3362.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1987</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1987H_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1987</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1987_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1986</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1986_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1986</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1986_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1985</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1985H_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1985</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1985_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1984</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1984H_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1984</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1984_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1983</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1983H_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1983</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1983_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1982</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1982H_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1982</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1982_Kjemi_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1981</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1981H_Kjemi_3321_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1981</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1981_Kjemi_3321_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1980</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1980H_Kjemi_3321_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1980</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1980_Kjemi_3321_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1979</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1979H_Kjemi_3321_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1979</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1979_Kjemi_3321_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1978</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1978H_Kjemi_3321_3361.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1978</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1978_Kjemi_A_Kj_AR_Kj_31.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>H1977</h3>
        </li>
        <li>
          <p>Oppgave (Mangler)</p>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
        <li>
          <h3>V1977</h3>
        </li>
        <li>
          <a href="/eksamensoppgaver/Kjemi 2/1977_Kjemi_A_Kj_AR_Kj_31.pdf" target="_blank" download>
            Oppgave</a>
        </li>
        <li>
          <p>Løsning (Mangler)</p>
        </li>
"""

base_path = r"G:\My Drive\Personal\Programming\Projects\OCR Question Bank\OCR-Question-Finder"

soup = BeautifulSoup(html_content, 'html.parser')
result = {}

# Parse the HTML content and create the dictionary
for h3 in soup.find_all('h3'):
    if len(h3.text) == 5:
        anchor = h3.find_next('a', href=True)
        if anchor and '/eksamensoppgaver/' in anchor['href']:
            full_path = base_path + anchor['href'].replace('/', '\\')
            full_path = full_path.replace('\\\\', '\\').replace('\\', '/')
            result[h3.text] = full_path

# Rename the files according to the specified format and update the HTML content
for key, path in result.items():
    # Extract the directory and the file extension
    directory, old_filename = os.path.split(path)
    file_extension = os.path.splitext(old_filename)[1]
    
    # Create the new filename
    new_filename = f"Eksamen_{subject}_{key}{file_extension}"
    
    # Create the full path for the new filename
    new_path = os.path.join(directory, new_filename)
    
    # Rename the file, ignoring case sensitivity
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower() == old_filename.lower():
                os.rename(os.path.join(root, file), new_path)
                print(f"Renamed '{os.path.join(root, file)}' to '{new_path}'")
                break
    
    # Update the anchor tag in the HTML content
    for anchor in soup.find_all('a', href=True):
        if anchor['href'].lower().endswith(old_filename.lower()):
            anchor['href'] = anchor['href'].replace(old_filename, new_filename)

# Write the updated HTML content to a text file
updated_html_content = soup.prettify()
with open("updated_html_content.txt", "w", encoding="utf-8") as file:
    file.write(updated_html_content)

print("Updated HTML content has been written to 'updated_html_content.txt'")
