<script>
    // Centro aproximado del Lago Llanquihue
    const centerLat = -41.13;
    const centerLon = -72.95;
    const zoomLevel = 11;

    // Límites aproximados del Lago Llanquihue (rectángulo)
    // (ajusta si quieres más o menos margen)
    const lakeBounds = L.latLngBounds(
        L.latLng(-41.40, -73.25),  // suroeste (lat, lon)
        L.latLng(-40.90, -72.60)   // noreste (lat, lon)
    );

    // Crear mapa
    const map = L.map('map', {
        center: [centerLat, centerLon],
        zoom: zoomLevel,
        maxBounds: lakeBounds,          // 🔒 no salir de esta zona
        maxBoundsViscosity: 1.0,        // "pared invisible" fuerte
        minZoom: 10                     // evita alejarse demasiado
    });

    // Asegurarse que el mapa encaje en los límites
    map.fitBounds(lakeBounds);

    // Capa base (OpenStreetMap)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    // ================================
    // 1) LUGARES DE INTERÉS (marcadores)
    // ================================
    const lugaresInteres = [
        {
            nombre: "Puerto Varas",
            lat: -41.3183,
            lon: -72.9854,
            descripcion: "Ciudad turística a orillas del Lago Llanquihue."
        },
        {
            nombre: "Frutillar",
            lat: -41.1239,
            lon: -73.0515,
            descripcion: "Frutillar: teatro del lago y vista a los volcanes."
        },
        {
            nombre: "Puerto Octay",
            lat: -41.1126,
            lon: -72.9014,
            descripcion: "Localidad patrimonial a orillas del lago."
        }
    ];

    lugaresInteres.forEach(lugar => {
        L.marker([lugar.lat, lugar.lon])
            .addTo(map)
            .bindPopup(`<b>${lugar.nombre}</b><br>${lugar.descripcion}`);
    });

    // ================================
    // 2) ZONA DE COBERTURA (ejemplo)
    // ================================
    const cobertura = L.circle([-41.30, -72.97], {
        radius: 7000, // en metros
        color: "#1976d2",
        fillColor: "#1976d2",
        fillOpacity: 0.18
    }).addTo(map);

    cobertura.bindPopup("Zona de cobertura TuristLake (ejemplo)");

    // ================================
    // 3) POLÍGONO (otra zona)
    // ================================
    const zonaPoligono = L.polygon([
        [-41.25, -72.92],
        [-41.22, -72.86],
        [-41.19, -72.90]
    ], {
        color: "#ff9800",
        fillColor: "#ff9800",
        fillOpacity: 0.2
    }).addTo(map);

    zonaPoligono.bindPopup("Zona de interés especial (ejemplo)");
</script>
