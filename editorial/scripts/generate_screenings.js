async function produce(tools,cfg){
 const repo=cfg.repo,from=cfg.from,to=cfg.to;
 const manifest=JSON.parse((await tools.mcp__GitHub__fetch_file({repository_full_name:repo,path:"manifest.json"})).result.content);
 const rows=manifest.chapters.filter(x=>x.number>=from&&x.number<=to);
 const src=await Promise.all(rows.map(x=>tools.mcp__GitHub__fetch_file({repository_full_name:repo,path:x.path})));
 const trim=x=>x.replace(/\\s+/g," ").replace(/\\|/g,"\\\\|").replace(/`/g,"'").slice(0,230);
 const entries=[],summary=[];
 for(let i=0;i<rows.length;i++){
  const r=rows[i],n=r.number,L=src[i].result.content.split("\\n"),body=L.filter((x,j)=>j!==0&&x.trim()!=="---").join(" "),words=body.trim().split(/\\s+/).filter(Boolean).length;
  const c=L.map((s,j)=>({line:j+1,t:s.trim()})).filter(x=>x.line>2&&x.t.length>=75&&!x.t.startsWith("#")&&!x.t.startsWith('"')&&!x.t.startsWith("—"));
  const anchor=[0.12,0.48,0.84].map(f=>c[Math.floor((c.length-1)*f)]).filter(Boolean);
  const link=v=>"../../"+r.path+"#L"+v;
  let doc="# Chapter "+String(n).padStart(3,"0")+" editorial screening: "+r.title+"\\n\\n";
  doc+="**Source:** [Chapter "+n+"](../../"+r.path+"), git blob `"+src[i].result.sha+"`. **Approximate body words:** "+words.toLocaleString("en-US")+". **Status:** Screening only; manuscript unchanged.\\n\\n";
  doc+="**Review standard:** FIC_CONTEXT.md. Full text scanned for the checks below; representative scenes used for editorial checkpoints. Not a certification of exhaustive close reading.\\n\\n";
  doc+="## Chapter-specific focus\\n\\n"+(cfg.focus[String(n)]||"Ensure this chapter's principal activity produces a distinct emotional or practical consequence.")+"\\n\\n";
  doc+="## Source passages for scene-level review\\n\\n";
  const qs=["**Opening development:** Which present objective, social friction or physical constraint gives the activity stakes beyond established belonging?",
  "**Middle development:** Does the event change someone's knowledge, choice or behavior, or merely restate a feeling already established?",
  "**Closing handoff:** Identify what concretely persists: promise, new boundary, object, visit, recovery, project milestone or unresolved conflict."];
  for(let k=0;k<anchor.length;k++){const a=anchor[k];doc+=(k+1)+". "+qs[k]+" **[Line "+a.line+"]("+link(a.line)+"):** “"+trim(a.t)+(a.t.length>230?"…":"")+"”\\n\\n";}
  doc+="## Mechanical and continuity flags\\n\\n";
  let checks=0;
  const phrases=["the whole of it","shifting his weight against the cold","the weight of","we'll figure it out","the tenth lantern","the winter was coming","the heel was getting looked at","it was enough"];
  for(const p of phrases){const at=L.flatMap((x,j)=>x.toLowerCase().includes(p)?[j+1]:[]);if(at.length>=3){checks++;doc+="- **Verified repeated phrase:** `"+p+"` appears on "+at.length+" lines, e.g. "+at.slice(0,4).map(z=>"[L"+z+"]("+link(z)+")").join(", ")+". Review its function before selectively cutting.\\n";}}
  const markers=L.flatMap((x,j)=>/^###\\s*(?:POV|Percy|Annabeth|Thalia|Silena|Clarisse|EVERYONE)/i.test(x)?[j+1]:[]);
  if(markers.length){checks++;doc+="- **Formatting:** Explicit narrator labels at "+markers.slice(0,6).map(z=>"[L"+z+"]("+link(z)+")").join(", ")+". Replace with clear limited scenes and unlabeled breaks.\\n";}
  const bad=L.flatMap((x,j)=>/\\b(?:I've to|you've to|Did you've|studied at her)\\b/i.test(x)?[j+1]:[]);
  if(bad.length){checks++;doc+="- **Grammar review:** Nonstandard contractions or phrasing at "+bad.slice(0,6).map(z=>"[L"+z+"]("+link(z)+")").join(", ")+". Inspect exact dialogue and fix contextually.\\n";}
  const exact=new Map();let duplicates=[];
  for(let j=0;j<L.length;j++){const t=L[j].trim().replace(/\\s+/g," ");if(t.split(" ").length<24)continue;let old=exact.get(t);if(old!==undefined){duplicates.push([old,j+1,t]);}else exact.set(t,j+1);}
  if(duplicates.length){checks++;doc+="- **Confirmed identical long lines within chapter:** "+duplicates.slice(0,3).map(d=>"[L"+d[0]+"]("+link(d[0])+") and [L"+d[1]+"]("+link(d[1])+")").join("; ")+". Compare surrounding scenes before rewriting the later occurrence.\\n";}
  if(n>=140&&words<10000){checks++;doc+="- **Confirmed length gap:** "+words.toLocaleString("en-US")+" body words is below the stated 10,000-word per-chapter floor for the Chapter 140+ drafting stretch. Expand only with earned, substantive development.\\n";}
  if(n>=101&&n<=114){checks++;doc+="- **Confirmed structural seam:** Chapter "+n+" is only "+words.toLocaleString("en-US")+" body words; Chapters 101–114 are much shorter than adjacent volumes. Decide whether to retain as a titled interlude, join with an adjacent scene, or expand meaningfully.\\n";}
  if(n===133||n===136||n===137){checks++;doc+="- **Age checkpoint:** The birthday/age progression in Chapters 133, 136 and 137 must be reconciled against the 14-year baseline from Chapter 140.\\n";}
  if([80,139,144,148,149,162,163,169,190].includes(n)){checks++;doc+="- **Cross-chapter duplication candidate:** This chapter contains text that matches passages in distant chapters. Check a whole-manuscript sliding-window duplicate report before changing either scene; do not globally delete repeated lines.\\n";}
  if(!checks)doc+="- No flagged constructions were detected by these selected mechanical checks; this **does not** demonstrate the chapter is error-free.\\n";
  let mentions=["Jason","Tyson","Triton","Amphitrite","Beryl","Zeus","Rhys"].map(name=>({name,line:L.findIndex(x=>new RegExp("\\\\b"+name+"\\\\b","i").test(x))+1})).filter(x=>x.line>0);
  if(mentions.length)doc+="- **Continuity names:** "+mentions.slice(0,5).map(x=>x.name+" ([L"+x.line+"]("+link(x.line)+"))").join(", ")+". A mention does not prove physical presence; verify travel, communication or recollection in the local scene.\\n";
  doc+="\\n## Canon boundaries and follow-through\\n\\nPercy/Clarisse/Silena are Poseidon half-siblings; Thalia/Annabeth Grace are Zeus daughters and sisters. Only Percy and Annabeth remember the displaced future. Percy and Annabeth's younger relationship remains nonsexual. Later Thalia/Rhys scenes concern two adults. Keep the rewrite architect unknown. Track dates, injuries, visitors and gifts with the surrounding chapter, and preserve original text until an authorized revision.\\n\\n**Audit status:** Evidence-linked screening, not an implemented fix.\\n";
  entries.push({path:"editorial/audits/chapter-"+String(n).padStart(3,"0")+".md",mode:"100644",type:"blob",content:doc});
  summary.push({n,words,checks,report_chars:doc.length});
 }
 const tree=await tools.mcp__GitHub__create_tree({repository_full_name:repo,base_tree_sha:cfg.base_tree_sha,tree_elements:entries});
 return {tree:tree.result.sha,from,to,count:entries.length,summary};
}
produce