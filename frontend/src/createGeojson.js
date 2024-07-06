// [
//     37.3, 37.9, 55.55, 55.95
// ],

const coords = [
    {
        name: "1",
        coordinates: [37.3, 37.5, 55.55, 55.69]
    },
    {
        name: "2",
        coordinates: [37.5, 37.7, 55.55, 55.69]
    },
    {
        name: "3",
        coordinates: [37.7, 37.9, 55.55, 55.69]
    },
    {
        name: "4",
        coordinates: [37.3, 37.5, 55.69, 55.83]
    },
    {
        name: "5",
        coordinates: [37.5, 37.7, 55.69, 55.83]
    },
    {
        name: "6",
        coordinates: [37.7, 37.9, 55.69, 55.83]
    },
    {
        name: "7",
        coordinates: [37.3, 37.5, 55.83, 55.97]
    },
    {
        name: "8",
        coordinates: [37.5, 37.7, 55.83, 55.97]
    },
    {
        name: "9",
        coordinates: [37.7, 37.9, 55.83, 55.97]
    }
]


export default function getGeojson(){
    let result = {
        "type": "FeatureCollection",
        "features": []
    }
    

    coords.forEach(element => {
        result.features.push({
            "id": element.name,
            "type": "Feature",
            "properties": {
                "name": element.name
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [element.coordinates[0], element.coordinates[3]],
                        [element.coordinates[0], element.coordinates[2]],
                        [element.coordinates[1], element.coordinates[2]],
                        [element.coordinates[1], element.coordinates[3]],
                        [element.coordinates[0], element.coordinates[3]],
                    ]
                    ],
            }
        })
    });


    


    return result;
   
};