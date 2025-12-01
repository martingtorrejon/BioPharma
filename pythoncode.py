import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
# Create a map centered on Italy
m = folium.Map(location=[42.5, 12.5], zoom_start=6)
marker_cluster = MarkerCluster().add_to(m)

# Dictionary of City Coordinates (Lat, Lon) based on the image's locations
city_coords = {
    "Abano Terme": [45.3592, 11.7891],
    "Agrate Brianza": [45.5770, 9.3550],
    "Alghero": [40.5579, 8.3193],
    "Ancona": [43.6158, 13.5189],
    "Aprilia": [41.5954, 12.6517],
    "Ascoli": [42.8553, 13.5749],
    "Ascoli Piceno": [42.8553, 13.5749],
    "Baranzate": [45.5273, 9.1245],
    "Bergamo": [45.6983, 9.6773],
    "Bologna": [44.4949, 11.3426],
    "Brescia": [45.5416, 10.2118],
    "Bresso": [45.5380, 9.1880],
    "Bruino": [45.0256, 7.4727],
    "Calco": [45.7236, 9.4180],
    "Cameri": [45.5033, 8.6477],
    "Campobello di Mazara": [37.6394, 12.7428],
    "Campoverde": [41.5333, 12.7167], # Campoverde di Aprilia
    "Caponago": [45.5714, 9.3789],
    "Caronno Pertusella": [45.5997, 9.0433],
    "Cartoceto": [43.7656, 12.9356],
    "Carugate": [45.5516, 9.3364],
    "Catania": [37.5079, 15.0830],
    "Cerano": [45.4124, 8.7844],
    "Ceriano Laghetto": [45.6322, 9.0836],
    "Chieti": [42.3510, 14.1675],
    "Chignolo di'Isola": [45.6667, 9.5333],
    "Cinisello Balsam": [45.5583, 9.2132], # Cinisello Balsamo
    "Colleretto Giacosa": [45.4328, 7.8286],
    "Crespellano-Valsamoggia": [44.5122, 11.1306],
    "Desio": [45.6186, 9.2064],
    "Faenza": [44.2854, 11.8830],
    "Ferentino": [41.6922, 13.2561],
    "Firenze": [43.7696, 11.2558],
    "Florence": [43.7696, 11.2558],
    "Formello": [42.0811, 12.4005],
    "Gallarate": [45.6606, 8.7944],
    "Genoa": [44.4056, 8.9463],
    "Gropello": [45.2075, 8.9950], # Gropello Cairoli likely
    "Grosotto": [46.2817, 10.2742],
    "Guidonia Montecelio": [41.9967, 12.7239],
    "Isola della Scala": [45.2694, 11.0089],
    "Isso": [45.5222, 9.7567],
    "Jesi": [43.5186, 13.2428],
    "L'Aquila": [42.3498, 13.3995],
    "L'Aquilo": [42.3498, 13.3995], # Typo fix
    "Latina": [41.4676, 12.9038],
    "Latina Scalo": [41.5333, 12.9333],
    "Mailand": [45.4642, 9.1900], # Milan
    "Marostica": [45.7461, 11.6569],
    "Masate": [45.5683, 9.4319],
    "Mereto di Tomba": [46.0486, 13.0381],
    "Milan": [45.4642, 9.1900],
    "Milano": [45.4642, 9.1900],
    "Modena": [44.6471, 10.9252],
    "Monsano": [43.5636, 13.2464],
    "Monteriggioni": [43.3896, 11.2238],
    "Monteroni D'Arbia": [43.2300, 11.4244],
    "Monza": [45.5845, 9.2744],
    "Naples": [40.8518, 14.2681],
    "Napoli": [40.8518, 14.2681],
    "Nerviano": [45.5561, 8.9744],
    "Novara": [45.4469, 8.6212],
    "Origgio": [45.5969, 9.0169],
    "Ozzano dell'Emilia": [44.4444, 11.4789],
    "Paderno Dugnano": [45.5719, 9.1678],
    "Padova": [45.4064, 11.8768],
    "Padua": [45.4064, 11.8768],
    "Parma": [44.8015, 10.3279],
    "Paullo": [45.4247, 9.3986],
    "Pavia": [45.1849, 9.1583],
    "Pennabilli": [43.8186, 12.2683],
    "Perugia": [43.1107, 12.3908],
    "Pessano con Bornago": [45.5517, 9.3828],
    "Piombino-Dese": [45.6072, 11.0028],
    "Pisa": [43.7228, 10.4017],
    "Pomezia": [41.6696, 12.5015],
    "Porto Mantovano": [45.1950, 10.7967],
    "Pozzuoli": [40.8224, 14.1186],
    "Reggello": [43.6833, 11.5333],
    "Rodano": [45.4850, 9.3517],
    "Roma": [41.9028, 12.4964],
    "Rome": [41.9028, 12.4964],
    "Rozzano": [45.3853, 9.1550],
    "Saluggia": [45.2407, 8.0163],
    "Sassari": [40.7259, 8.5556],
    "Scandicci": [43.7567, 11.1842],
    "Scorzè": [45.5722, 12.1100],
    "Sesto Fiorentino": [43.8324, 11.1965],
    "Siena": [43.3188, 11.3308],
    "Sovicille": [43.2800, 11.2294],
    "Sovizzo": [45.5267, 11.4553],
    "Taranto": [40.4638, 17.2470],
    "Torino": [45.0703, 7.6869]
}

# List of Companies and Cities extracted from the image
data = [
    ("Fidia Farmaceutici", "Abano Terme"), ("ACS DOBFAR", "Agrate Brianza"), ("Virostatics", "Alghero"),
    ("Angelini Pharma", "Ancona"), ("Recordati", "Aprilia"), ("Pfizer", "Ascoli"), ("Pfizer", "Ascoli Piceno"),
    ("Dipharma", "Baranzate"), ("Famar", "Baranzate"), ("CordenPharma", "Bergamo"), ("Alfasigma", "Bologna"),
    ("CellPly", "Bologna"), ("Recipharm", "Brescia"), ("Roncadelle Operations", "Brescia"), ("AGC Biologics", "Bresso"),
    ("AGC Biologics", "Bresso"), ("Newron Pharmaceuticals", "Bresso"), ("Sibylla Biotech", "Bresso"), ("Zambon", "Bresso"),
    ("INTRAUMA", "Bruino"), ("Charles River Laboratories", "Calco"), ("Procos", "Cameri"),
    ("Gesan Production", "Campobello di Mazara"), ("AbbVie", "Campoverde"), ("AbbVie", "Campoverde"),
    ("Adienne Pharma and Biotech", "Caponago"), ("CordenPharma", "Caponago"), ("CordenPharma", "Caponago"),
    ("Dipharma", "Caronno Pertusella"), ("Diatheva", "Cartoceto"), ("Aenova", "Carugate"), ("Etna Biotech", "Catania"),
    ("Delpharm", "Cerano"), ("TRIFARMA", "Ceriano Laghetto"), ("MediaPharma", "Chieti"), ("Flamma", "Chignolo di'Isola"),
    ("Italfarmaco Research", "Cinisello Balsam"), ("AorticLab", "Colleretto Giacosa"),
    ("Siare Engineering", "Crespellano-Valsamoggia"), ("Opis Research", "Desio"), ("GreenBone Ortho", "Faenza"),
    ("Patheon", "Ferentino"), ("Menarini", "Firenze"), ("Hospitex International", "Florence"), ("Menarini", "Florence"),
    ("Lumenis", "Formello"), ("Biofarma Group", "Gallarate"), ("SI-BONE", "Gallarate"), ("Esaote", "Genoa"),
    ("IAMA Therapeutics", "Genoa"), ("Eye Pharma", "Genoa"), ("Axplora", "Gropello"), ("Baxter", "Grosotto"),
    ("Adaltis", "Guidonia Montecelio"), ("Fresenius Kabi", "Isola della Scala"), ("Flamma", "Isso"),
    ("Diatech Pharmacogenetics", "Jesi"), ("Dompé", "L'Aquila"), ("Menarini", "L'Aquila"), ("Loto Biotech", "L'Aquilo"),
    ("Aenova", "Latina"), ("BSP Pharmaceuticals", "Latina Scalo"), ("Bayer", "Mailand"), ("Igenomix", "Marostica"),
    ("Recipharm", "Masate"), ("Biofarma Group", "Mereto di Tomba"), ("Dipharma", "Mereto di Tomba"),
    ("AAVantgarde Bio", "Milan"), ("Adare Pharma Solutions", "Milan"), ("Altheia Science", "Milan"),
    ("Aptadir", "Milan"), ("Axxam", "Milan"), ("BetaGlue Therapeutics", "Milan"), ("BioClec", "Milan"),
    ("Biofarma Group", "Milan"), ("BMG Pharma", "Milan"), ("Borea Therapeutics", "Milan"), ("Bracco", "Milan"),
    ("CaSRevolution", "Milan"), ("CheckMab", "Milan"), ("Cytosens", "Milan"), ("Delpharm", "Milan"), ("Dompé", "Milan"),
    ("Empatica", "Milan"), ("Enthera Pharmaceuticals", "Milan"), ("Farmaka", "Milan"), ("Genenta Science", "Milan"),
    ("Genespire", "Milan"), ("Indena", "Milan"), ("InnovHeart", "Milan"), ("Integra LifeSciences", "Milan"),
    ("Italfarmaco Research", "Milan"), ("Lipogems International", "Milan"), ("Monteresearch", "Milan"),
    ("NanoPhoria Bioscience", "Milan"), ("NEURO-ZONE", "Milan"), ("Newronika", "Milan"), ("Norgine", "Milan"),
    ("NTC", "Milan"), ("PinCell", "Milan"), ("Recordati", "Milan"), ("Sentinel Diagnostics", "Milan"),
    ("Sintesi Research", "Milan"), ("Sprim", "Milan"), ("StemGen/HyperStem", "Milan"), ("Labospace", "Milano"),
    ("Holostem Terapie Avanzate", "Modena"), ("Opocrin", "Modena"), ("Chema Diagnostica", "Monsano"),
    ("DIESSE Diagnostica Senese", "Monteriggioni"), ("Philogen", "Monteriggioni"), ("Galenica Senese", "Monteroni D'Arbia"),
    ("Patheon", "Monza"), ("RhemaStem", "Monza"), ("Roche", "Monza"), ("Roche", "Monza"),
    ("Rottapharm Biotech", "Monza"), ("Dompé", "Naples"), ("Cytosens", "Napoli"),
    ("Nerviano Medical Sciences", "Nerviano"), ("Chemlectiva", "Novara"), ("Grunenthal", "Origgio"),
    ("Biogenera", "Ozzano dell'Emilia"), ("Recipharm", "Paderno Dugnano"), ("Biofarma Group", "Padova"),
    ("AB ANALITICA", "Padua"), ("BMR Genomics", "Padua"), ("Chiesi", "Parma"), ("preclinics", "Parma"),
    ("Cambrex", "Paullo"), ("EnGenome", "Pavia"), ("Valpharma", "Pennabilli"), ("Plasfer", "Perugia"),
    ("Steroglass", "Perugia"), ("Adare Pharma Solutions", "Pessano con Bornago"), ("Stevanato Group", "Piombino-Dese"),
    ("Abiogen", "Pisa"), ("Farmigea", "Pisa"), ("Medical Microinstruments", "Pisa"), ("Advaxia Biologics", "Pomezia"),
    ("IRBM", "Pomezia"), ("Solaris Biotech", "Porto Mantovano"), ("InnovaVector", "Pozzuoli"), ("PQE Group", "Reggello"),
    ("Olon", "Rodano"), ("Probiomics", "Roma"), ("Angelini Pharma", "Rome"), ("CrestOptics", "Rome"),
    ("Dornier MedTech", "Rome"), ("Exiris", "Rome"), ("Genechron", "Rome"), ("Lo.Li. Pharma", "Rome"),
    ("Neomatrix", "Rome"), ("Nouscom", "Rome"), ("Omikron Italia", "Rome"), ("ReiThera", "Rome"), ("Takis", "Rome"),
    ("Worldwide Clinical Trials", "Rome"), ("TRIFARMA", "Rozzano"), ("DiaSorin", "Saluggia"), ("MicroPort", "Saluggia"),
    ("Virostatics", "Sassari"), ("Molteni Farmaceutici", "Scandicci"), ("Molteni Therapeutics", "Scandicci"),
    ("I-Tech Medical Division", "Scorzè"), ("Eli Lilly", "Sesto Fiorentino"), ("BiOMViS", "Siena"), ("EXOSOMICS", "Siena"),
    ("Lead Discovery Siena", "Siena"), ("Philogen", "Sovicille"), ("Brevetti CEA", "Sovizzo"),
    ("iVis Technologies", "Taranto"), ("Kither Biotech", "Torino")
]

# Generate markers
for company, city in data:
    if city in city_coords:
        coords = city_coords[city]
        
        # Add a very small jitter to prevent identical points from covering each other perfectly when zoomed in,
        # or just let MarkerCluster handle it (MarkerCluster handles stacking well).
        # We will use MarkerCluster strictly.
        
        label_text = f"{company} - {city}"
        
        folium.Marker(
            location=coords,
            popup=folium.Popup(label_text, parse_html=True),
            tooltip=label_text,
            icon=folium.Icon(color='blue', icon='flask', prefix='fa')
        ).add_to(marker_cluster)

m.save("italy_pharma_map.html")
st_folium(m, width=1800, height=800)
