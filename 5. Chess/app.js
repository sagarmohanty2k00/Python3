const heigh = 900/8;
const width = 900/8;

const border = 10;

// Set Up the board
// white
const wp1 = document.getElementById('wp1')
const wp2 = document.getElementById('wp2')
const wp3 = document.getElementById('wp3')
const wp4 = document.getElementById('wp4')
const wp5 = document.getElementById('wp5')
const wp6 = document.getElementById('wp6')
const wp7 = document.getElementById('wp7')
const wp8 = document.getElementById('wp8')

const wb2 = document.getElementById('wb2')
const wb1 = document.getElementById('wb1')
const wr1 = document.getElementById('wr1')
const wr2 = document.getElementById('wr2')
const wk1 = document.getElementById('wk1')
const wk2 = document.getElementById('wk2')
const wqueen = document.getElementById('wqueen')
const wking = document.getElementById('wking')

wp1.style.top = `${6*heigh + border}px`
wp1.style.left = `${width*0 + border}px`

wp2.style.top = `${6*heigh + border}px`
wp2.style.left = `${width*1 + border}px`

wp3.style.top = `${6*heigh + border}px`
wp3.style.left = `${width*2 + border}px`

wp4.style.top = `${6*heigh + border}px`
wp4.style.left = `${width*3 + border}px`

wp5.style.top = `${6*heigh + border}px`
wp5.style.left = `${width*4 + border}px`

wp6.style.top = `${6*heigh + border}px`
wp6.style.left = `${width*5 + border}px`

wp7.style.top = `${6*heigh + border}px`
wp7.style.left = `${width*6 + border}px`

wp8.style.top = `${6*heigh + border}px`
wp8.style.left = `${width*7 + border}px`


wb1.style.top = `${7*heigh + border}px`
wb1.style.left = `${width*2 + border}px`

wb2.style.top = `${7*heigh + border}px`
wb2.style.left = `${width*5 + border}px`

wr1.style.top = `${7*heigh + border}px`
wr1.style.left = `${width*7 + border}px`

wr2.style.top = `${7*heigh + border}px`
wr2.style.left = `${width*0 + border}px`

wk1.style.top = `${7*heigh + border}px`
wk1.style.left = `${width*1 + border}px`

wk2.style.top = `${7*heigh + border}px`
wk2.style.left = `${width*6 + border}px`

wqueen.style.top = `${7*heigh + border}px`
wqueen.style.left = `${width*3 + border}px`

wking.style.top = `${7*heigh + border}px`
wking.style.left = `${width*4 + border}px`

// black
const bp1 = document.getElementById('bp1')
const bp2 = document.getElementById('bp2')
const bp3 = document.getElementById('bp3')
const bp4 = document.getElementById('bp4')
const bp5 = document.getElementById('bp5')
const bp6 = document.getElementById('bp6')
const bp7 = document.getElementById('bp7')
const bp8 = document.getElementById('bp8')

const bb1 = document.getElementById('bb1')
const bb2 = document.getElementById('bb2')
const br1 = document.getElementById('br1')
const br2 = document.getElementById('br2')
const bk1 = document.getElementById('bk1')
const bk2 = document.getElementById('bk2')
const bqueen = document.getElementById('bqueen')
const bking = document.getElementById('bking')

bp1.style.top = `${heigh + border}px`
bp1.style.left = `${width*0 + border}px`

bp2.style.top = `${heigh + border}px`
bp2.style.left = `${width*1 + border}px`

bp3.style.top = `${heigh + border}px`
bp3.style.left = `${width*2 + border}px`

bp4.style.top = `${heigh + border}px`
bp4.style.left = `${width*3 + border}px`

bp5.style.top = `${heigh + border}px`
bp5.style.left = `${width*4 + border}px`

bp6.style.top = `${heigh + border}px`
bp6.style.left = `${width*5 + border}px`

bp7.style.top = `${heigh + border}px`
bp7.style.left = `${width*6 + border}px`

bp8.style.top = `${heigh + border}px`
bp8.style.left = `${width*7 + border}px`


bb1.style.top = `${0*heigh + border}px`
bb1.style.left = `${width*2 + border}px`

bb2.style.top = `${0*heigh + border}px`
bb2.style.left = `${width*5 + border}px`

br1.style.top = `${0*heigh + border}px`
br1.style.left = `${width*7 + border}px`

br2.style.top = `${0*heigh + border}px`
br2.style.left = `${width*0 + border}px`

bk1.style.top = `${0*heigh + border}px`
bk1.style.left = `${width*1 + border}px`

bk2.style.top = `${0*heigh + border}px`
bk2.style.left = `${width*6 + border}px`

bqueen.style.top = `${0*heigh + border}px`
bqueen.style.left = `${width*3 + border}px`

bking.style.top = `${0*heigh + border}px`
bking.style.left = `${width*4 + border}px`

// The board
let board = new Array(8)
for (let i=0; i<8; i++) {
    let b = new Array(8)
    for (let j=0; j<8; j++) {
        b[j] = "";
    }
    board[i] = b;
}

// set initial position


// highlighted area
let highlighted = new Array(1)
function highligh() {
    
}

function onSelect(id) {
    // check whea
}

