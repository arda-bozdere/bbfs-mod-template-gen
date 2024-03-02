<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mod ID Generator</title>
</head>
<body>
    <script>
        // Function to prompt the user and store the result in a file
        function promptAndStore(promptMessage, fileName) {
            const userInput = prompt(promptMessage).toLowerCase();
            const blob = new Blob([userInput], { type: "text/plain;charset=utf-8" });
            saveAs(blob, fileName);
            return userInput;
        }

        // Function to generate the JSON file
        function generateJSON(modName, devName, itemCount) {
            const modData = {
                modName: modName,
                modDev: devName,
                items: []
            };

            for (let i = 1; i <= itemCount; i++) {
                const itemType = prompt(`Item ${i}: Is it an accessory (type 1) or a skin (type 2)?`);
                const imgName = prompt(`Item ${i} PNG name:`);
                const itemName = prompt(`Item ${i} name:`).toLowerCase().replace(/[\s.]/g, '');
                const itemId = `net.${devName}.${modName}.${itemName}`;

                modData.items.push({
                    itemId: itemId,
                    itemName: itemName,
                    itemPNG: imgName
                });
            }

            const jsonData = JSON.stringify(modData, null, 2);
            const blob = new Blob([jsonData], { type: "application/json;charset=utf-8" });
            saveAs(blob, "modData.json");
        }

        // Main script
        const modName = promptAndStore("What is your mod's name (no spaces or dots, full lowercase)?", "modName.txt");
        const devName = promptAndStore("What is your development name (no spaces or dots, full lowercase)?", "devName.txt");
        const itemCount = parseInt(prompt("How many items will this mod add?"));

        if (isNaN(itemCount) || itemCount <= 0) {
            alert("Invalid input for item count. Please enter a positive integer.");
        } else {
            generateJSON(modName, devName, itemCount);
        }
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js"></script>
</body>
</html>
