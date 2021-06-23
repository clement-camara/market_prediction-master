import pandas as pd


class BasicModel:
    def __init__(self, df, indicator, activity, portefeuille, portefeuille_frais, frais):
        self.frais = frais
        self.total_frais = 0
        market_activity = 1
        portefeuille_perso = df.Close[0]
        portefeuille_perso_frais = df.Close[0]
        index = -1
        last_adj_close = df.Close[0]

        for df_element in df.values:
            index += 1
            adj_close = df_element[4]
            date = df_element[0]
            pourcent_var = (adj_close-last_adj_close) /last_adj_close
            
            if market_activity == 1:
                
                portefeuille_perso = portefeuille_perso + (portefeuille_perso*pourcent_var)
                portefeuille_perso_frais = portefeuille_perso_frais + (portefeuille_perso_frais*pourcent_var)
            
                try:
                    if df[indicator][index-1] > df[indicator][index] :
                        market_activity = 0
                        self.total_frais += frais
                        portefeuille_perso_frais -= frais
                        print(f"{date} || GO SELL || {index} || {adj_close} || {portefeuille_perso} || {portefeuille_perso_frais}")
                except:
                    pass
                
            try:
                if df[indicator][index-1] < df[indicator][index] and market_activity == 0:
                    market_activity = 1
                    self.total_frais += frais
                    portefeuille_perso_frais -= frais
                    print(f"{date} || GO BUY || {index} || {adj_close}|| {portefeuille_perso} || {portefeuille_perso_frais}\n")
            except:
                pass

            if portefeuille_perso_frais < 0:
                portefeuille_perso_frais = 0

            df.iloc[index, df.columns.get_loc(portefeuille)] = portefeuille_perso
            df.iloc[index, df.columns.get_loc(portefeuille_frais)] = portefeuille_perso_frais
            df.iloc[index, df.columns.get_loc(activity)] = market_activity
            #df.iloc[index, 10] = indicator
            last_adj_close = adj_close
            self.df = df

    def stats(self, portefeuille, portefeuille_frais):
        print(f"Départ : {int(self.df[portefeuille][0])}€\n\nStratégie sans frais final : {int(self.df[portefeuille][-1:].values[0])}€\nStratégie avec frais final: {int(self.df[portefeuille_frais][-1:].values[0])}€\nSans stratégie final: {int(self.df['Close'][-1:].values[0])}€\n\nTotal frais: {int(self.total_frais)}€\nTotal transactions: {int(self.total_frais/self.frais)}")








class InverseModel:
    def __init__(self, df, indicator, activity, portefeuille, portefeuille_frais, frais):
        self.frais = frais
        self.total_frais = 0
        market_activity = 1
        portefeuille_perso = df.Close[0]
        portefeuille_perso_frais = df.Close[0]
        index = -1
        last_adj_close = df.Close[0]

        for df_element in df.values:
            index += 1
            adj_close = df_element[4]
            date = df_element[0]
            pourcent_var = (adj_close-last_adj_close) /last_adj_close
        
            if market_activity == 1:
                portefeuille_perso = portefeuille_perso + (portefeuille_perso*pourcent_var)
                portefeuille_perso_frais = portefeuille_perso_frais + (portefeuille_perso_frais*pourcent_var)

                try:
                    if df[indicator][index-1] < df[indicator][index] :
                        market_activity = 0
                        self.total_frais += frais
                        portefeuille_perso_frais -= frais
                        print(f"{date} || GO SELL || {index} || {adj_close} || {portefeuille_perso} || {portefeuille_perso_frais}")
                except:
                    pass
                
            try:
                if df[indicator][index-1] > df[indicator][index] and market_activity == 0:
                    market_activity = 1
                    self.total_frais += frais
                    #portefeuille_perso = portefeuille_perso + (portefeuille_perso*pourcent_var)
                    #portefeuille_perso_frais = portefeuille_perso_frais + (portefeuille_perso_frais*pourcent_var)
                    portefeuille_perso_frais -= frais
                    print(f"{date} || GO BUY || {index} || {adj_close}|| {portefeuille_perso} || {portefeuille_perso_frais}\n")
            except:
                pass

            if portefeuille_perso_frais < 0:
                portefeuille_perso_frais = 0
            df.iloc[index, df.columns.get_loc(portefeuille)] = portefeuille_perso
            df.iloc[index, df.columns.get_loc(portefeuille_frais)] = portefeuille_perso_frais
            df.iloc[index, df.columns.get_loc(activity)] = market_activity
            #df.iloc[index, 10] = indicator
            last_adj_close = adj_close
            self.df = df

    def stats(self, portefeuille, portefeuille_frais):
        print(f"Départ : {int(self.df[portefeuille][0])}€\n\nStratégie sans frais final : {int(self.df[portefeuille][-1:].values[0])}€\nStratégie avec frais final: {int(self.df[portefeuille_frais][-1:].values[0])}€\nSans stratégie final: {int(self.df['Close'][-1:].values[0])}€\n\nTotal frais: {int(self.total_frais)}€\nTotal transactions: {int(self.total_frais/self.frais)}")







class RSIModel:
    def __init__(self, df, indicator, activity, portefeuille, portefeuille_frais, frais, rsi_sell_sup, rsi_buy_inf):
        self.frais = frais
        self.total_frais = 0
        market_activity = 1
        portefeuille_perso = df.Close[0]
        portefeuille_perso_frais = df.Close[0]
        index = -1
        last_adj_close = df.Close[0]
        for df_element in df.values:
            index += 1
            adj_close = df_element[4]
            date = df_element[0]
            pourcent_var = (adj_close-last_adj_close) /last_adj_close
            
            if market_activity == 1: 
                portefeuille_perso = portefeuille_perso + (portefeuille_perso*pourcent_var)
                portefeuille_perso_frais = portefeuille_perso_frais + (portefeuille_perso_frais*pourcent_var)
                
                try:
                    if df[indicator][index-1] > df[indicator][index] and df[indicator][index] > rsi_sell_sup :#condition sell
                        market_activity = 0
                        self.total_frais += frais
                        portefeuille_perso_frais -= frais
                        print(f"{date} || GO SELL || {index} || {adj_close} || {portefeuille_perso} || {portefeuille_perso_frais}")
                except:
                    pass
                
            try:
                if df[indicator][index-1] < df[indicator][index] and market_activity == 0 and df[indicator][index] < rsi_buy_inf :#condition buy
                    market_activity = 1
                    self.total_frais += frais
                    portefeuille_perso_frais -= frais
                    print(f"{date} || GO BUY || {index} || {adj_close}|| {portefeuille_perso} || {portefeuille_perso_frais}\n")
            except:
                pass
            if portefeuille_perso_frais < 0:
                portefeuille_perso_frais = 0
            df.iloc[index, df.columns.get_loc(portefeuille)] = portefeuille_perso
            df.iloc[index, df.columns.get_loc(portefeuille_frais)] = portefeuille_perso_frais
            df.iloc[index, df.columns.get_loc(activity)] = market_activity
            #df.iloc[index, 10] = indicator
            last_adj_close = adj_close
            self.df = df
    def stats(self, portefeuille, portefeuille_frais):
        print(f"Départ : {int(self.df[portefeuille][0])}€\n\nStratégie sans frais final : {int(self.df[portefeuille][-1:].values[0])}€\nStratégie avec frais final: {int(self.df[portefeuille_frais][-1:].values[0])}€\nSans stratégie final: {int(self.df['Close'][-1:].values[0])}€\n\nTotal frais: {int(self.total_frais)}€\nTotal transactions: {int(self.total_frais/self.frais)}")




class SuperModel:
    def __init__(self, df, indicator, activity, portefeuille, portefeuille_frais, frais, buy_signal, sell_signal):
        self.frais = frais
        self.total_frais = 0
        market_activity = 1
        portefeuille_perso = df.Close[0]
        portefeuille_perso_frais = df.Close[0]
        index = -1
        last_adj_close = df.Close[0]

        for df_element in df.values:
            index += 1
            adj_close = df_element[4]
            date = df_element[0]
            pourcent_var = (adj_close-last_adj_close) /last_adj_close
            
            if market_activity == 1:
                
                portefeuille_perso = portefeuille_perso + (portefeuille_perso*pourcent_var)
                portefeuille_perso_frais = portefeuille_perso_frais + (portefeuille_perso_frais*pourcent_var)
            
                try:
                    if df[indicator][index] <= sell_signal :
                        market_activity = 0
                        self.total_frais += frais
                        portefeuille_perso_frais -= frais
                        print(f"{date} || GO SELL || {index} || {adj_close} || {portefeuille_perso} || {portefeuille_perso_frais}")
                except:
                    pass
                
            try:
                if df[indicator][index] >= buy_signal and market_activity == 0:
                    market_activity = 1
                    self.total_frais += frais
                    portefeuille_perso_frais -= frais
                    print(f"{date} || GO BUY || {index} || {adj_close}|| {portefeuille_perso} || {portefeuille_perso_frais}\n")
            except:
                pass

            if portefeuille_perso_frais < 0:
                portefeuille_perso_frais = 0

            df.iloc[index, df.columns.get_loc(portefeuille)] = portefeuille_perso
            df.iloc[index, df.columns.get_loc(portefeuille_frais)] = portefeuille_perso_frais
            df.iloc[index, df.columns.get_loc(activity)] = market_activity
            #df.iloc[index, 10] = indicator
            last_adj_close = adj_close
            self.df = df

    def stats(self, portefeuille, portefeuille_frais):
        print(f"Départ : {int(self.df[portefeuille][0])}€\n\nStratégie sans frais final : {int(self.df[portefeuille][-1:].values[0])}€\nStratégie avec frais final: {int(self.df[portefeuille_frais][-1:].values[0])}€\nSans stratégie final: {int(self.df['Close'][-1:].values[0])}€\n\nTotal frais: {int(self.total_frais)}€\nTotal transactions: {int(self.total_frais/self.frais)}")

