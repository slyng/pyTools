'''
Created on 29/giu/2013

@author: lys

Cifrario VIC

Il cifrario VIC e' un cifrario carta e penna utilizzato dalla spia sovietica
Reino Hayhanen, il cuo nome in codice era "VICTOR". Al momento della sua scoperta
era senz'altro il piu' complesso cifrario implementato manualmente mai visto:
le conclusioni dell'analisi iniziale fatta dall'NSA nel 1953 non indicavano in alcun
modo che esso potesse essere un cifrario manuale ma il fatto di averlo ritrovato
in una monetina cava da 5 centesimi poteva far supporre che potesse essere risolto 
con il semplice uso di carta e penna.
Il cifrario VIC rimanse inviolato fino a quando non 
furono disponibili maggiori informazioni sulla sua struttura.
Anche se non cosi' complessi o sicuri come i piu' recenti cifrari digitali 
utilizzabili sui moderni computer, i messaggi scritti con il cifrario VIC in pratica
resistettero a tutti i tentativi di crittanalisi condotti dall'NSA dal 1953 al 1957,
anno in cui Hayhanen tradi' il suo Paese e chiese asilo politico al governo americano.
'''

class VIC:
    '''
    Classe che descrive il cifrario VIC
    '''
    _SCELTA_CH_EXTRA = "-+#_/\?!%&"
    
    def __init__(self, chiave='et aon ris', extra='-/'):
        '''
        Inizializzazione del cifrario
        di default la chiave e' "et aon ris"
        '''
        self.scacchiera = []
        self.chiave = chiave
        self.extra = self._get_extra(extra)
        self._genera_scacchiera()
        
    def _get_extra(self, s):
        '''
        Verifica se i 2 caratteri extra da inserire siano
        compresi nell'alfabeto o uno di simboli permessi
        '''
        e = ''
        for x in s:
            if x in self._SCELTA_CH_EXTRA:
                e += x
            else:
                print "error carattere non permesso"
        if len(e) >= 2:
            e = e[:2]
        else:
            print "error non hai inserti sufficienti caratteri extra validi"
        print e
        return e
    
    def _genera_scacchiera(self):
        if self.chiave:
            import string
            s = []
            s.extend( string.ascii_lowercase + self.extra )
            s0 = []
            s0.extend(self.chiave)
            for x in self.chiave:
                if not x == ' ':
                    del s[s.index(x)]
                    print x, s
            s0[self.chiave.index(' ')] = s[:10]
            s0[self.chiave.rindex(' ')] = s[-10:]
            print s0
            
        else:
            print "error problemi con la generazione di scacchiera"

if __name__ == "__main__":
    vic = VIC()