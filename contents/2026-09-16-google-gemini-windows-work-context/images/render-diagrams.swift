import AppKit
let dir = CommandLine.arguments[1]
let ink = NSColor(calibratedRed:0.09,green:0.16,blue:0.20,alpha:1)
let teal = NSColor(calibratedRed:0.12,green:0.43,blue:0.43,alpha:1)
let muted = NSColor(calibratedRed:0.42,green:0.47,blue:0.47,alpha:1)
let cream = NSColor(calibratedRed:0.95,green:0.94,blue:0.89,alpha:1)
let ochre = NSColor(calibratedRed:0.78,green:0.48,blue:0.19,alpha:1)
func box(_ x:CGFloat,_ y:CGFloat,_ w:CGFloat,_ h:CGFloat,_ color:NSColor,_ radius:CGFloat=22){color.setFill();NSBezierPath(roundedRect:NSRect(x:x,y:y,width:w,height:h),xRadius:radius,yRadius:radius).fill()}
func label(_ s:String,_ x:CGFloat,_ y:CGFloat,_ w:CGFloat,_ size:CGFloat=30,_ color:NSColor=ink,_ bold:Bool=false){
 let p=NSMutableParagraphStyle();p.lineSpacing=8
 let font=NSFont(name:bold ? "AppleSDGothicNeo-Bold" : "AppleSDGothicNeo-Medium",size:size) ?? NSFont.systemFont(ofSize:size)
 (s as NSString).draw(in:NSRect(x:x,y:y,width:w,height:200),withAttributes:[.font:font,.foregroundColor:color,.paragraphStyle:p])
}
func line(_ x:CGFloat,_ y:CGFloat,_ xx:CGFloat,_ yy:CGFloat,_ c:NSColor=teal){c.setStroke();let p=NSBezierPath();p.lineWidth=5;p.move(to:NSPoint(x:x,y:y));p.line(to:NSPoint(x:xx,y:yy));p.stroke()}
func arrow(_ x:CGFloat,_ y:CGFloat,_ xx:CGFloat,_ yy:CGFloat){line(x,y,xx,yy);line(xx-12,yy-12,xx,yy);line(xx-12,yy+12,xx,yy)}
func doc(_ x:CGFloat,_ y:CGFloat,_ w:CGFloat,_ h:CGFloat,_ accent:NSColor){box(x,y,w,h,.white,12);box(x+20,y+20,12,h-40,accent,6);for k in 0..<3{box(x+50,y+28+CGFloat(k)*28,w-75,6,cream,3)}}
func render(_ n:Int,_ suffix:String,_ h:Int,_ draw:()->Void){
 let rep=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:1080,pixelsHigh:h,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0)!
 let cg=NSGraphicsContext(bitmapImageRep:rep)!.cgContext
 cg.translateBy(x:0,y:CGFloat(h));cg.scaleBy(x:1,y:-1)
 NSGraphicsContext.saveGraphicsState();NSGraphicsContext.current=NSGraphicsContext(cgContext:cg,flipped:true)
 box(0,0,1080,CGFloat(h),cream,0);label(String(format:"%02d",n)+" / WORK CONTEXT",64,42,800,22,teal,true)
 draw();label("Humaiin 자체 제작 개념도 · 실제 제품 화면 아님",64,CGFloat(h == 1350 ? 605 : 600),950,21,muted)
 NSGraphicsContext.restoreGraphicsState()
 try! rep.representation(using:.png,properties:[:])!.write(to:URL(fileURLWithPath:dir+"/google-gemini-work-context-"+String(format:"%02d",n)+"-"+suffix+"-v1.png"))
}
render(2,"shortcut",1350){
 box(70,135,940,410,ink,32)
 label("작업 중인 자리에서",112,164,800,32,.white,true)
 box(125,257,240,170,cream);label("Alt",200,297,190,62,ink,true)
 label("+",394,299,70,60,.white)
 box(495,257,445,170,cream);label("Space",592,297,350,62,ink,true)
 label("Gemini 호출",395,466,400,30,NSColor.white,true)
}
render(3,"context-selection",650){
 doc(65,170,160,180,ochre);doc(102,221,160,180,teal);label("여러 원본",93,450,230,29,muted)
 arrow(286,315,374,315)
 box(394,150,285,325,teal);label("선택 기준",442,183,240,39,.white,true)
 label("업무 목적\n자료의 범위\n최신 버전",445,260,220,31,.white)
 arrow(700,315,784,315)
 doc(812,212,190,200,teal);label("사용할 근거",805,450,230,29,muted)
}
render(4,"brief-workflow",650){
 let xs:[CGFloat]=[64,330,596,862]
 let names=["자료 지정","초안 요청","원문 대조","공유 판단"]
 let subs=["범위·기간","결정 / 미결","누락·상충","사람의 책임"]
 for i in 0..<4{let x=xs[i];box(x,195,154,154,i==2 ? ochre : teal,28);label(String(i+1),x+51,224,110,64,.white,true);label(names[i],x-12,385,215,31,ink,true);label(subs[i],x-18,439,220,24,muted);if i<3{arrow(x+171,270,x+239,270)}}
}
render(6,"review-skills",650){
 let names=["자료 선택","요청 설계","근거 검증","공유 판단"]
 let desc=["무엇을 볼 것인가","무엇을 구분할 것인가","원문과 일치하는가","누가 확인했는가"]
 for i in 0..<4{let x:CGFloat=i%2==0 ? 64 : 566;let y:CGFloat=i<2 ? 130 : 365;box(x,y,450,198,.white);box(x+25,y+28,64,64,i%2==0 ? teal : ochre,18);label(String(i+1),x+43,y+37,55,37,.white,true);label(names[i],x+110,y+32,300,35,ink,true);label(desc[i],x+30,y+121,410,27,muted)}
}
render(7,"comparison-exercise",650){
 box(64,145,425,370,.white);box(591,145,425,370,.white)
 label("A  자유 요청",97,182,380,38,ink,true);label("B  범위 지정",622,182,380,38,teal,true)
 doc(105,273,335,137,ochre);doc(635,273,335,137,teal)
 label("“요약해줘”",137,441,330,29,muted);label("기간 + 파일 + 출력 기준",620,441,395,27,muted)
 label("VS",509,290,80,32,ochre,true)
 label("비교할 것: 누락 · 근거 · 수정 부담",235,548,700,26,ink,true)
}
