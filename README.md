# ⚽ Zamora CF – Portal de Scouting

> Plataforma profesional de análisis de rendimiento, gestión de jugadores y scouting para el Zamora CF.

![Version](https://img.shields.io/badge/versión-2.0-red) ![Status](https://img.shields.io/badge/estado-activo-green) ![Liga](https://img.shields.io/badge/liga-1ª%20RFEF-blue)

---

## 🌐 Acceso

| Plataforma | URL |
|---|---|
| Netlify | https://spontaneous-tulumba-0deb84.netlify.app |
| GitHub Pages | https://RoberDev22.github.io/zamora-cf-scouting |

---

## 📋 Índice

- [Funcionalidades](#-funcionalidades)
- [Secciones de la app](#-secciones-de-la-app)
- [Base de datos](#-base-de-datos)
- [Cuentas de acceso](#-cuentas-de-acceso)
- [Edición con Python](#-edición-con-python)
- [Tecnologías](#-tecnologías)

---

## ✨ Funcionalidades

### 🔐 Sistema de Login
- Inicio de sesión con **nombre de usuario o email**
- Opción **"Recuérdame"** para mantener la sesión activa en el navegador
- **Creación de cuenta** nueva directamente desde el login (nombre, email, contraseña y rol)
- Validaciones de duplicados y formato de email

---

### 📊 Dashboard
Panel principal con resumen en tiempo real de toda la actividad del portal:

- **Tarjetas de estadísticas** → total de jugadores, favoritos del scout, valoración media y contratos urgentes
- **Alertas de contratos** → jugadores con contrato que vence en menos de 180 días con acceso directo
- **Top valorados** → ranking de los 4 jugadores con mayor puntuación scout
- **Añadidos recientemente** → últimas incorporaciones a la cartera
- **Jugadores por liga** → desglose visual de jugadores según competición

---

### 👥 Cartera de Jugadores
Gestión completa de la base de datos de jugadores:

#### Filtros y búsqueda
- Búsqueda por **nombre, club o nacionalidad**
- Filtro por **liga** (1ª RFEF, Hypermotion, LaLiga, 5 Grandes Ligas, La Liga, Premier League, Champions League, Bundesliga, Serie A)
- Filtro por **posición** (11 posiciones disponibles)
- Filtro por **fuente** (Manual, Wyscout, StatsBomb)

#### Ficha de jugador
Cada jugador dispone de una ficha completa con:
- **Estadísticas** → goles, asistencias, partidos, minutos, xG y nota media
- **Información** → club, liga, pie dominante, edad, valor de mercado, altura, peso, fin de contrato y estado de préstamo
- **Valoración scout** → puntuación del 1 al 10 con indicador visual
- **Gráfico radar** → representación visual de rendimiento en 5 dimensiones
- **Barras de estadísticas** → visualización comparativa de goles, asistencias, xG y partidos
- **Notas del scout** → observaciones personalizadas
- **Enlace de vídeo** → acceso directo a material audiovisual
- **Informes de partido vinculados** → historial de informes asociados al jugador

#### Acciones por jugador
- ⭐ **Marcar como favorito** → cada scout tiene su propia lista de favoritos
- ⚖️ **Comparar** → selecciona dos jugadores para ver una comparativa lado a lado
- 📄 **Exportar PDF** → genera un informe profesional en PDF con todos los datos e informes
- ✏️ **Editar** → modificar cualquier dato del jugador
- 🗑️ **Eliminar** → eliminar con confirmación de seguridad

---

### ⚖️ Comparativa de Jugadores
Herramienta de comparación visual entre dos jugadores:

- **Tarjetas de perfil** de cada jugador con posición, club y valoración
- **Barras dobles enfrentadas** para goles, asistencias, xG, partidos y minutos
- Código de color diferenciado (rojo vs azul) para identificar a cada jugador

---

### ⚠️ Alertas de Contratos
Sistema de notificaciones para contratos próximos a vencer:

- **🔴 Urgente** → contratos que vencen en menos de 90 días
- **🟡 Atención** → contratos que vencen entre 90 y 180 días
- Badge de alerta en el menú lateral con el número de contratos urgentes
- Aviso en el Dashboard con acceso directo a la sección

---

### 📋 Informes de Partido
Sistema completo de generación de informes de observación:

Cada informe recoge:
- **Jugador observado** → búsqueda en tiempo real por nombre o club
- **Datos del partido** → fecha, rival, competición y minutos observados
- **Nota del partido** → valoración del 1 al 10 con selector visual
- **Observaciones generales** → descripción del rendimiento
- **Fortalezas** → aspectos positivos destacados
- **Aspectos a mejorar** → puntos débiles o áreas de desarrollo

Los informes aparecen vinculados en la ficha del jugador y se incluyen en la exportación PDF.

---

### 📄 Exportación PDF
Genera un informe profesional en PDF con:

- **Cabecera** con nombre, posición, club y branding del Zamora CF
- **Fila de estadísticas** destacadas
- **Información completa** del jugador en formato cuadrícula
- **Notas del scout**
- **Informes de partido** asociados al jugador
- Pie de página con fecha de generación

---

### 🔭 Perfiles de Scouts
Gestión del equipo de scouting:

- Vista de todos los scouts registrados con su rol y favoritos
- Indicador visual del **perfil propio** del usuario activo
- Lista de **jugadores favoritos** por scout con su valoración
- **Crear nuevos scouts** directamente desde la app

---

## 🗄️ Base de Datos

La app integra **2.000+ jugadores** de múltiples fuentes:

| Fuente | Liga | Jugadores |
|---|---|---|
| Wyscout | 1ª RFEF | 500 |
| Wyscout | Hypermotion | 500 |
| Wyscout | LaLiga | 500 |
| Wyscout | 5 Grandes Ligas | 500 |
| StatsBomb Open Data | La Liga, Premier League, Champions League, Bundesliga, Serie A | Variable* |

*Los datos de StatsBomb se cargan automáticamente al abrir la app si hay conexión a internet. Se cachean localmente durante 7 días.

### Datos disponibles por jugador (Wyscout)
`nombre · club · posición · edad · valor de mercado · fin de contrato · nacionalidad · pie dominante · altura · peso · préstamo · goles · minutos · xG`

---

## 📥 Importar datos externos

### Importar desde Wyscout (CSV)
1. Exporta jugadores desde Wyscout → **Export → CSV**
2. Ve a la sección **Import Wyscout** en la app
3. Sube el archivo CSV
4. Mapea las columnas automáticamente
5. Previsualiza e importa

### StatsBomb Open Data
La sección **StatsBomb** permite explorar y añadir jugadores de:
- La Liga · Premier League · UEFA Champions League · Bundesliga · Serie A
- Botón de recarga para forzar actualización de datos
- Filtro por liga y búsqueda por nombre o club
- Importación selectiva por jugador

---

## 🔑 Cuentas de Acceso

| Usuario | Contraseña | Rol |
|---|---|---|
| Carlos Fernández | scout123 | Head Scout |
| Ana Martínez | scout456 | Analista Scout |
| Diego Ruiz | scout789 | Scout Territorial |

> Puedes crear nuevas cuentas desde la pantalla de login → "Crear cuenta"

---

## 🐍 Edición con Python

El repositorio incluye un kit de herramientas Python para modificar los datos de la app:

```
zamora_editor.py      → Script principal con todas las funciones
zamora_players.json   → Base de datos de 2.000 jugadores
zamora_scouts.json    → Configuración de scouts
```

### Funciones disponibles

```python
# CONSULTA
buscar_jugador(jugadores, "López")
filtrar_por_liga(jugadores, "LaLiga")
filtrar_por_posicion(jugadores, "Delantero Centro")
filtrar_por_edad(jugadores, 18, 23)
top_por_valoracion(jugadores, n=10)
estadisticas_liga(jugadores)
contratos_proximos(jugadores, dias=90)

# MODIFICACIÓN
añadir_jugador(jugadores, {...})
actualizar_valoracion(jugadores, "Nombre", 9)
añadir_nota(jugadores, "Nombre", "Observación...")
eliminar_jugador(jugadores, "Nombre")
añadir_scout(scouts, "Nombre", "password", "Rol")

# EXPORTAR A LA APP
regenerar_html(jugadores, scouts)
```

### Uso rápido

```bash
# 1. Instalar dependencias (ninguna externa necesaria, solo Python 3)
python3 --version

# 2. Ejecutar el script
python3 zamora_editor.py

# 3. Hacer cambios (editar el script y descomentar ejemplos)
# 4. Regenerar el HTML con los cambios
```

---

## 🛠️ Tecnologías

| Tecnología | Uso |
|---|---|
| React 18 | Framework de interfaz |
| Babel Standalone | Compilación JSX en navegador |
| jsPDF | Exportación de informes PDF |
| Inter (Google Fonts) | Tipografía |
| Lucide Icons (SVG) | Sistema de iconos |
| StatsBomb Open Data | Datos abiertos de fútbol profesional |
| LocalStorage | Persistencia de datos local |
| Netlify / GitHub Pages | Hosting gratuito |

---

## 📁 Estructura del repositorio

```
zamora-cf-scouting/
├── index.html            # App completa (HTML + React + datos)
├── zamora_editor.py      # Script Python para editar datos
├── zamora_players.json   # Base de datos de jugadores (JSON)
├── zamora_scouts.json    # Configuración de scouts (JSON)
└── README.md             # Esta documentación
```

---

## 🚀 Próximos pasos

- [ ] Integración con **Supabase** para datos compartidos en tiempo real entre scouts
- [ ] Sistema de notificaciones push para alertas de contratos
- [ ] Módulo de comparativa avanzada con datos históricos
- [ ] Exportación de informes en formato Excel

---

*Desarrollado para el Zamora CF · Portal de Scouting v2.0*
