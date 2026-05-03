"""
╔══════════════════════════════════════════════════════════╗
║     ZAMORA CF SCOUTING – Script de práctica Python       ║
║     Modifica los datos y vuelve a generar el HTML        ║
╚══════════════════════════════════════════════════════════╝

INSTRUCCIONES:
1. Coloca este script en la misma carpeta que:
   - index.html
   - zamora_players.json
   - zamora_scouts.json
2. Ejecuta: python3 zamora_editor.py
3. Se generará un nuevo index.html con tus cambios
"""

import json
import re

# ─────────────────────────────────────────────────────────
# 1. CARGAR DATOS
# ─────────────────────────────────────────────────────────

def cargar_jugadores(ruta="zamora_players.json"):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def cargar_scouts(ruta="zamora_scouts.json"):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_jugadores(jugadores, ruta="zamora_players.json"):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(jugadores, f, ensure_ascii=False, indent=2)
    print(f"✓ Guardados {len(jugadores)} jugadores en {ruta}")

def guardar_scouts(scouts, ruta="zamora_scouts.json"):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(scouts, f, ensure_ascii=False, indent=2)
    print(f"✓ Guardados {len(scouts)} scouts en {ruta}")


# ─────────────────────────────────────────────────────────
# 2. FUNCIONES DE CONSULTA (practica aquí lectura de datos)
# ─────────────────────────────────────────────────────────

def buscar_jugador(jugadores, nombre):
    """Busca jugadores por nombre (parcial, sin distinguir mayúsculas)"""
    nombre = nombre.lower()
    resultados = [j for j in jugadores if nombre in j["name"].lower()]
    return resultados

def filtrar_por_liga(jugadores, liga):
    """Filtra jugadores por liga"""
    return [j for j in jugadores if j.get("liga") == liga]

def filtrar_por_posicion(jugadores, posicion):
    """Filtra jugadores por posición"""
    return [j for j in jugadores if j.get("position") == posicion]

def filtrar_por_edad(jugadores, edad_min, edad_max):
    """Filtra jugadores por rango de edad"""
    return [j for j in jugadores if edad_min <= j.get("age", 0) <= edad_max]

def top_por_valoracion(jugadores, n=10):
    """Devuelve los N jugadores con mayor valoración scout"""
    con_rating = [j for j in jugadores if j.get("scoutRating", 0) > 0]
    return sorted(con_rating, key=lambda j: j["scoutRating"], reverse=True)[:n]

def estadisticas_liga(jugadores):
    """Muestra cuántos jugadores hay por liga"""
    from collections import Counter
    ligas = [j.get("liga", "Sin liga") for j in jugadores]
    return dict(Counter(ligas))

def contratos_proximos(jugadores, dias=180):
    """Jugadores con contrato que vence en menos de X días"""
    from datetime import datetime, timedelta
    limite = datetime.now() + timedelta(days=dias)
    resultado = []
    for j in jugadores:
        contrato = j.get("contractEnd", "")
        if contrato:
            try:
                fecha = datetime.strptime(contrato, "%Y-%m-%d")
                if fecha <= limite:
                    resultado.append({**j, "dias_restantes": (fecha - datetime.now()).days})
            except:
                pass
    return sorted(resultado, key=lambda x: x["dias_restantes"])


# ─────────────────────────────────────────────────────────
# 3. FUNCIONES DE MODIFICACIÓN (practica aquí escritura)
# ─────────────────────────────────────────────────────────

def añadir_jugador(jugadores, nuevo_jugador):
    """
    Añade un jugador nuevo. Estructura mínima:
    {
        "name": "Nombre Apellido",
        "age": 23,
        "nationality": "Español",
        "position": "Delantero Centro",
        "club": "Zamora CF",
        "liga": "1ª RFEF",
        "foot": "Derecho",
        "contractEnd": "2026-06-30",
        "scoutRating": 7,
        "notes": "Notas del scout",
        "marketValue": "500K €",
        "stats": {"goals": 10, "assists": 3, "matches": 25, "minutes": 1800, "xg": 8.5, "rating": 7.0}
    }
    """
    import time
    nuevo_jugador.setdefault("id", f"p{int(time.time())}")
    nuevo_jugador.setdefault("source", "manual")
    nuevo_jugador.setdefault("addedBy", "python")
    nuevo_jugador.setdefault("addedAt", "2025-01-01")
    nuevo_jugador.setdefault("videoLinks", "")
    nuevo_jugador.setdefault("height", 0)
    nuevo_jugador.setdefault("weight", 0)
    nuevo_jugador.setdefault("onLoan", False)
    nuevo_jugador.setdefault("positionRaw", "")
    nuevo_jugador.setdefault("stats", {"goals":0,"assists":0,"matches":0,"minutes":0,"xg":0,"rating":0})
    jugadores.append(nuevo_jugador)
    print(f"✓ Jugador añadido: {nuevo_jugador['name']}")
    return jugadores

def actualizar_valoracion(jugadores, nombre, nueva_valoracion):
    """Actualiza la valoración scout de un jugador"""
    for j in jugadores:
        if j["name"].lower() == nombre.lower():
            j["scoutRating"] = nueva_valoracion
            print(f"✓ Valoración de {j['name']} actualizada a {nueva_valoracion}/10")
            return jugadores
    print(f"✗ Jugador '{nombre}' no encontrado")
    return jugadores

def añadir_nota(jugadores, nombre, nota):
    """Añade una nota a un jugador"""
    for j in jugadores:
        if j["name"].lower() == nombre.lower():
            j["notes"] = nota
            print(f"✓ Nota añadida a {j['name']}")
            return jugadores
    print(f"✗ Jugador '{nombre}' no encontrado")
    return jugadores

def eliminar_jugador(jugadores, nombre):
    """Elimina un jugador por nombre"""
    antes = len(jugadores)
    jugadores = [j for j in jugadores if j["name"].lower() != nombre.lower()]
    if len(jugadores) < antes:
        print(f"✓ Jugador '{nombre}' eliminado")
    else:
        print(f"✗ Jugador '{nombre}' no encontrado")
    return jugadores

def añadir_scout(scouts, nombre, password, rol="Scout"):
    """Añade un nuevo scout"""
    import time
    initials = "".join(p[0] for p in nombre.split()[:2]).upper()
    scouts.append({
        "id": f"s{int(time.time())}",
        "name": nombre,
        "password": password,
        "role": rol,
        "avatar": initials,
        "favorites": []
    })
    print(f"✓ Scout añadido: {nombre}")
    return scouts


# ─────────────────────────────────────────────────────────
# 4. REGENERAR EL HTML (inyectar los datos modificados)
# ─────────────────────────────────────────────────────────

def regenerar_html(jugadores, scouts, html_entrada="index.html", html_salida="index.html"):
    """
    Inyecta los datos modificados de vuelta en el HTML.
    ¡Esto actualiza la app con tus cambios!
    """
    with open(html_entrada, "r", encoding="utf-8") as f:
        html = f.read()

    # Reemplazar DB_PLAYERS
    idx = html.find("const DB_PLAYERS=")
    start = html.find("[", idx)
    depth = 0
    end = start
    for i, c in enumerate(html[start:], start):
        if c == '[': depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0: end = i; break

    nuevo_json = json.dumps(jugadores, ensure_ascii=False)
    html = html[:start] + nuevo_json + html[end+1:]

    # Reemplazar DEFAULT_SCOUTS
    idx2 = html.find("const DEFAULT_SCOUTS=")
    start2 = html.find("[", idx2)
    depth = 0
    end2 = start2
    for i, c in enumerate(html[start2:], start2):
        if c == '[': depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0: end2 = i; break

    nuevo_scouts = json.dumps(scouts, ensure_ascii=False)
    html = html[:start2] + nuevo_scouts + html[end2+1:]

    with open(html_salida, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ HTML regenerado: {html_salida} ({len(html)//1024}KB)")
    print(f"  → {len(jugadores)} jugadores · {len(scouts)} scouts")


# ─────────────────────────────────────────────────────────
# 5. EJEMPLOS PRÁCTICOS (descomenta los que quieras probar)
# ─────────────────────────────────────────────────────────

if __name__ == "__main__":

    # ── Cargar datos ──────────────────────────────────────
    jugadores = cargar_jugadores()
    scouts = cargar_scouts()

    print(f"\n{'='*50}")
    print(f"  ZAMORA CF SCOUTING – Editor Python")
    print(f"{'='*50}")
    print(f"  Jugadores cargados: {len(jugadores)}")
    print(f"  Scouts cargados:    {len(scouts)}")
    print(f"{'='*50}\n")

    # ── EJEMPLO 1: Ver estadísticas por liga ──────────────
    print("📊 Jugadores por liga:")
    for liga, n in estadisticas_liga(jugadores).items():
        print(f"   {liga}: {n}")

    # ── EJEMPLO 2: Buscar un jugador ──────────────────────
    print("\n🔍 Búsqueda de 'López':")
    resultados = buscar_jugador(jugadores, "López")
    for j in resultados[:3]:
        print(f"   {j['name']} – {j['position']} – {j['club']}")

    # ── EJEMPLO 3: Top jugadores de LaLiga ────────────────
    print("\n⭐ Jóvenes promesas (sub-21) en LaLiga:")
    jovenes = filtrar_por_edad(filtrar_por_liga(jugadores, "LaLiga"), 0, 21)
    for j in jovenes[:5]:
        print(f"   {j['name']} ({j['age']}) – {j['position']} – {j['club']}")

    # ── EJEMPLO 4: Contratos próximos a vencer ────────────
    print("\n⚠️  Contratos que vencen en 90 días:")
    proximos = contratos_proximos(jugadores, dias=90)
    for j in proximos[:5]:
        print(f"   {j['name']} – {j['dias_restantes']} días – {j['club']}")

    # ── EJEMPLO 5: Añadir un jugador nuevo ────────────────
    # jugadores = añadir_jugador(jugadores, {
    #     "name": "Roberto Moreno",
    #     "age": 25,
    #     "nationality": "Español",
    #     "position": "Mediapunta",
    #     "club": "Zamora CF",
    #     "liga": "1ª RFEF",
    #     "foot": "Derecho",
    #     "contractEnd": "2026-06-30",
    #     "scoutRating": 8,
    #     "notes": "Gran visión de juego. Excelente pase largo.",
    #     "marketValue": "800K €",
    #     "stats": {"goals": 7, "assists": 11, "matches": 28, "minutes": 2200, "xg": 5.3, "rating": 7.4}
    # })

    # ── EJEMPLO 6: Actualizar valoración ─────────────────
    # jugadores = actualizar_valoracion(jugadores, "Z. Vanheusden", 8)

    # ── EJEMPLO 7: Añadir nota a un jugador ──────────────
    # jugadores = añadir_nota(jugadores, "Z. Vanheusden", "Muy buen central, gran salida de balón.")

    # ── EJEMPLO 8: Añadir nuevo scout ────────────────────
    # scouts = añadir_scout(scouts, "Roberto Moreno", "rob123", "Analista de Datos")

    # ── Guardar cambios y regenerar HTML ─────────────────
    # (Descomenta cuando hayas hecho cambios)
    # guardar_jugadores(jugadores)
    # guardar_scouts(scouts)
    # regenerar_html(jugadores, scouts)

    print("\n✅ Script ejecutado correctamente.")
    print("   Descomenta los ejemplos para hacer cambios y regenerar el HTML.\n")
