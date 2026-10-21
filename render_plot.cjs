// Optional publication-figure rasterizer; raw experiments need no npm packages.
const sharp = require('sharp');
const path = require('node:path');
sharp(path.join(__dirname,'pilot-coverage.svg'))
  .flatten({background:'white'})
  .png()
  .toFile(path.join(__dirname,'pilot-coverage.png'))
  .then(()=>console.log('Rendered pilot-coverage.png'))
  .catch(error=>{console.error(error.message);process.exitCode=1;});
