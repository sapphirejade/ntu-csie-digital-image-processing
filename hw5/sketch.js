let switchBtn, shiverBtn;
let alphaSlider;
let blendSelect;
let resetBtn;

let img1, img2;
let imageWidth = 512;
let imageHeight = 512;

let rectSize = 100;
let gridSize = 50;
let gridBias = 0;

function preload(){
  img1 = loadImage("hw5_1.jpg");
  img2 = loadImage("hw5_2.jpg");
}

function setup() {
  createCanvas(imageWidth, imageHeight);
  
  switchBtn = createButton("Switch");
  switchBtn.mousePressed(startSwitch);
  shiverBtn = createButton("Shiver");
  shiverBtn.mousePressed(startShiver);
  
  alphaSlider = createSlider(0,255,255);
  blendSelect = createSelect();
  blendSelect.option('BLEND', BLEND);
  blendSelect.option('ADD', ADD);     
  blendSelect.option('SCREEN', SCREEN);  
  blendSelect.option('REPLACE', REPLACE);  
  blendSelect.selected(BLEND);
  
  resetBtn = createButton("Reset");
  resetBtn.mousePressed(startReset);
}

function startSwitch() {
  temp = img1;
  img1 = img2;
  img2 = temp;
}

function startShiver() {
  if (gridBias>0) {
	gridBias=0;
  }else{
	gridBias+=noise(1)*5;
  }
}

function startReset() {
  gridBias = 0;
  loop();
  blendSelect.selected(BLEND);
}

function getPart() {
  if (mouseIsPressed == true && mouseButton == CENTER) {
    image(img2, 0, 0);
  } else {
    let part = img2.get(mouseX, mouseY, rectSize, rectSize);
    image(part, mouseX, mouseY, rectSize, rectSize);
  }
}

function draw(){
  blendMode(blendSelect.selected());
  background(0);
  for(let i = 0; i < 100; i++) {
    for(let j =0 ; j < 100; j++) {
      let x = i * imageWidth / gridSize;
      let y = j * imageHeight / gridSize;
      
      let c = color(img1.get(x, y));
      let c_density = round(
        red(c) * 0.222 + green(c) * 0.707 + blue(c) * 0.071
      );
      let radius = map(c_density, 0, 255, 2+random(3,5), 10+random(3,5));
      c.setAlpha(alphaSlider.value());
      fill(c);
      stroke(c);
      x = x + random(-gridBias, gridBias);
      y = y + random(-gridBias, gridBias);
      circle(x, y, radius);
    }
  }
  getPart();
}

function mouseMoved(){
  getPart();
}

function mousePressed(){
  if (mouseButton == LEFT) {
    gridSize = int(random(50, 100));
  }else if (mouseButton == RIGHT) {
    noLoop();
  }else if (mouseButton == CENTER) {
    
  }
}