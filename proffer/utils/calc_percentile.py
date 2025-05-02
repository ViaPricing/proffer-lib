import numpy as np

def calcular_percentil(valores, percentil=25):
    """
    Calcula o percentil de uma lista de valores.

    :param valores: lista ou array de números
    :param percentil: valor entre 0 e 100
    :return: valor do percentil
    """
    return np.percentile(valores, percentil)


def calcular_medias_por_grupo(response, grupo_alvo, campos_media):
    def calcular_media(lista):
        
        medias = {
            campo: round(sum(item[campo] for item in lista) / len(lista), 2)
            for campo in campos_media
        }

        for key in lista[0]:
            if key not in campos_media:
                medias[key] = lista[0][key]
        return medias

    grupo = [item for item in response if item.get("grupo") == grupo_alvo]
    indep = [item for item in response if item.get("grupo") != grupo_alvo]

    return {
        "grupo": calcular_media(grupo) if grupo else {},
        "independente": calcular_media(indep) if indep else {}
    }