import {classify, trainModel} from 'diagram-object-recognition' // just to prove that we can separate ML logic from the frontend part
import  p5 from 'p5';

var sketch = (p: p5) => {
  p.setup = () => {
    p.createCanvas(p.windowWidth, p.windowHeight);
  };

  p.draw = () => {
    p.background(0);
    p.fill(255);
    p.rect(100,100, 50, 50);
  };
};

new p5(sketch);