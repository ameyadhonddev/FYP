window.onload = init;

function init(){

    const mapElem = document.getElementById('mapid')

    const stadiaMaps = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    })

    const SmoothDark = L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
        maxZoom: 20,
        attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
    });
    const mymap = L.map(mapElem,{
        center: [0, 0],
        zoom: 5,
        minZoom: 4,
        layers: [stadiaMaps]
        /*layers: [
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            })
        ]*/
    })

    const baselayers = {
        'Smoothdark': SmoothDark,
        '<b>stadiaMaps</b>': stadiaMaps
    }

    const layerControls = L.control.layers(baselayers, {}, {
        position: 'topleft'
    }).addTo(mymap)

}