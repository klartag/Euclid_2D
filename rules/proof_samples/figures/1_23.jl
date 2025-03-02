Assumptions:
A, B, C, D, X, Y, Z: Point
distinct(A, B, C, D, X, Y, Z)
concyclic(A, B, C, D)
between(B, A, X)
between(C, D, X)
between(B, C, Y)
between(A, D, Y)
Line(X, Z) == internal_angle_bisector(A, X, D)
Line(Y, Z) == internal_angle_bisector(C, Y, D)

Embedding:
Y := {"x": "0.98219356280756608956750142169767059385776519775390625", "y": "0.187871778560218416487259673886001110076904296875"}
D := {"x": "-0.973288781337787067826639031409285962581634521484375", "y": "0.229584294153596990550880718728876672685146331787109375"}
C := {"x": "-0.7903986239881322095612858902313746511936187744140625", "y": "0.6125928625095686808066375306225381791591644287109375"}
B := {"x": "-1.3674056879738769683501218565373196449180182417083582138402761602981316801930233850725926458835601806640625", "y": "0.750846357863998471868152260460772300324209970222337152223507123101342575210992436041124165058135986328125"}
A := {"x": "-1.2689060161783025015265611604006604203662850332761285594578764032370213405038525859254060130375013828351659524372695935171780638789524009950639075956653431309143943514300480952529816612593843661012947028012223288344834666960869903155256232516593930415756600928631049445686258358393949012722733353868443851913515318250776951590340251329117327249767866231981615848360255015480510913986130569983943218481348812248826394910153172983216303940733181360504303341432054402182652226128024331330808620483633578859033099986735632775756364029942428111098852445225601555477991387234845378430193126489304725300870790041907210748139964521239257805816171834863206163920468484079504684471585865156175534310505060173620739065519952490133808190999457319295680716550351113245941976932603061302911137225956706280689193319016663850440224974536161796296471517072462026072355237089210330123195553031425914189670729196767129906967652661062341001905466092727416312536886653647800771689577626551428030400355011874339790390130182379396062251714772079943494215429607920196859719255366375202857226636419501869323373439082881655236175369224265764622137610787228706657371156906503007083620416742425787014937596271476104099106222188856671839142662053617898565104226875729153157068580617801858023938116370248064446498595304613400765615213673189587297873844222964219719700730516613234705321483546579789563742684637702194545929002029338628142506764877930902958789427121886609654903070810604001279635398335295880914115962782983040880047095269700873612802319432652887724739683640399648871554163312760161441525932394875719771819388807739468789850397940117105070053802465586072629891711241695118719218345917184148850182008591063234645158444473600153800243379775766039203853193229818780491795827210689280815452692535885779639375513996733665572732390707127110795837918559575213641183890941916676969802306308345787586067365621594040331836586216178451284108205919348055839400547130865634240131460211271972810587791442237647931667145829576248161", "y": "0.23589012378937706367778233078240061055281719576925644003391731952171658314579146710339685212436591597443003537390935371426963291940200094256975826657903261961562462668071121418127506063723581176371724171179736957747075205902022314265781588122576024512477374912165207804944514936314247152632578779096514223477810282682979745930986490848039916493359783563792056102758010763336840765005452688536286506747276172930918763137514196023353575121922256592206671999929814223383069860265773840798815011803912486963605484565041104311400451589408466558780054360527527891026188790561570466295766485603254458755214118170413650631934505543348035696806169179767444246382834461351125591314914602599000742805617092527885989732593943028433337843259417998393158167247346413435447748281623239091819359578835342570762378544820252791641375270921349000598804172825948205818666709032776080011076271446744046484458174430997935832418050834580277910214203900984023473984400291079473826236562545810709704150114740724400961018551272551894753027480706830323412196804960431255962527802158685268318257197290256761140458727329427207921447196355040504919299106951530813984029674955595124511002551805450219068828983118394827297308244057984776491473667541749616922734874010093635571182579455568007350368004917313261136206920091175065475452578687938634910667035067938707796244298391919550642359697305687908396009282271133621631043589282807641088238343873768980565159819647530524836330345592624445654258774116551656526198268263298217673177784632454987389937584074010982176232309753028539675666950774264416740925913886727625075141641993864926198616219405652307093529372697352216431296734115558312658975859145498361651285145957861399411634241225375719719017384931916825346579857115946538830077470910246444017098048787249215490962068089330569455245925313395959816340924983173165074777748086844113886141340299880714736865574087736177028521837210007468142298004154845357239052170474887892578817488661569518707019943064137314503114656814025196711"}
X := {"x": "-1.1834962367109182137429286073640661961262582837689488942352073345525031983215081312708405670151949831791146293199809367418822759677137061121097115855745176005397247953209047639011638469593850952339284928952656762751669618855169608122939283543023068180415050150182248710975501058077746845213647583740625637625740412623447201500133758281939559516138879586943884665458035174536340597835971106194684020564760597665034104039638954835739561114354845908429045501510777189946178582913371507345097213168101967353263971445037382638991078358808263775100953612675481715342499540975294790765794618329169036964094676538449955167508629451159352496961602888211458552090219934242088242480782135835001006907359446079779910097816122140204630014752303938458286737222654833401289240678764314619267576576427668360056201633998206727832211282859898088542634590958619189554931009957484006981562411609987304317741823206586106807916330269874459012694260350541939648127979376465707679394602150784392934276064850469761492450541169349055294668406039822579618766399258026789595811507039116126743044673397005502649098338228424235434308284073415139019820412764707437498488682894959788039086571175008985233941552855599125410635439491687350443052543274149713980749099731391959882138020129747917601477778422998024808522149911588129795644982078531939579475229775538611776453083487702072077781887249611104485484563137390241538887370172152108093288728416588532397162174458295098297256607755857418176321654923173144802055854555181337509950936868550598239312452987028849531287369417630188067548168845235288556406848180155849737813337561878609956399208390962927104996932900136390793913017087209027211165090896396162950418351819406334669281239686906934599018467593480717024802426813933807623335546486096337386872077075399989280903374811066163798428947384037667258584733570712209702925289236859341584206632137998198867634262157633286686229123421345109144677904155254488902320203668631655315939622293374823861800249698640730586896964035467305796", "y": "-0.21063215984775720609520958607786770749422499784195007385610100974263380333342936406442529479091712179023443159752187693830545639781059864365849602331209263501511418510817657013223033874746274626133128548954083854747663517918288499455618262720453128628543544609989361758698176948573998656831614651434267986153730336816276806504531922351613229935749347944778629338965464401564203338334492469927438468417720478181256165666248528013012908309970179213904166706039173258879354582204750709264615533478330775780672835445220351423163409195665610878177340469324358851459810712289812712617942287334958460584479522283702974182324738571225615565178023468494953933406919227433790874766636214470758125405716906214737238003877043403867966559808453226662936244115868137936202398141991963647446650309809820394459928109917752500124922965934896310619064235555349927244735043622055809543452720674122213529600022508214633684856667759903438159989727612610453144903762857472598220464590104622838713786010627773901648711917297606857143714926150909417015479825272315105055267404662754659853341373855440358425844464174733363185196858684590762395866850492575064273686599614664028223777771865553320318347630689969770256896539272117201251073907025763824046703215756758990642769346984027865356761211272901828494245495640819068025890309424963483483515236380133350576654757704228136567924444334950195529441522542886673781602242547232760818302441818300144969941812785159439742163028600414142400253652830718244055165295064102153651750245842633962374741279347573450353802439918889105258734658485689149409277315402423502749693195359817620953850114646482222032624576938498152711831056927349326409216757887803188539463772717344402045226751889995413719216023599240513387000979795613684479907328151546209440289561850877272950735740880021394018950404758327461239675552966309356546794785336216724908794721360063874626169714120609473930967992378548991350857321163486495957972296051460114446326327238328070341048107746959863182673577648359160598"}
Z := {"x": "-1.0975207068386926569932052234631285307473404151123830919983161762007071105628064781929262028213732354586692306856516923563017153555572035915602701645445596799395512164493179685972854962976605694956162011011102191094213510742421887362036896945782551074981474534347763412177657248269758475626214539739524330423606698731811757595683170028788811293513122507292496764831600948914736309036741992797282648734356836462980253488001750624939476425762130643715939938879176019443103072953487414873002610190142104554248681812651603323539882115797847291765432773500265129107110750172650305257322474233749588880435315082585216030759561584486765630552673135521459098457808257515399975579580306267819424446635124103353539578505030812188627012098825660251523388995938913946050846797903208146171030934193322141752699641273880366137842522920406307033404269915643198062152222963896056627364608952865786173884954345799627190313789809841959692542692839508175242026337231004067811383941738217233956963179065350057493224967047323613736856985270402096509821906682030084439183086936094526277751901697810763535253113265365170551293678464584897151799448647080744170475260988751666104784462619918956672522767484435587236765673656536071926044013608519199827655737102299381928020052187388862954230733432103572487103417082161829357494900674472154515454532353685451803796793218374438161501924921506484161946366881383433336726012922357918654328473079151906475708781117252916252342317186546608626900785849594156900028687698157483699747636674837472599820870375808819021494043959786722833323859048808652998234525743160499608752231974567327547127275021068075196687730433331560381061942717738518693900934424446053664291985414858750680514929476137455941620946707113173998130738893924680822332049701401858996128669733790442449822204231820762894314255511271717500362781427007342886459473160743828552721501304186040255363432900548129116149127219809833790516676291093016080955156080674537837304279162154970269932596333845760813910819540832576296", "y": "0.45606593838858507301225991024739348391779902356992078596157095889887383874181664160027450448854665540863804071206855413260904855917401924299348181008735550871848917549890882231259580942996616987498742319287521949855785643905607250771082425233518855611868600011655907902603847803834492002500717509346604219326618557441485827669832360024882312710925564809687065434308879632660306061720285579970070851809217476188949669030326178610621622386868810084274196243587409451322259781548812722621757056542712176430713143439607182407660734992196217345592034022673428526629471679742941851527236796430215344595246582603241608958822440332976071060147814375650073114084053002412590644627426952645548903680369854414344208976225549452890793358849491356396858472526290603352554565215710493432220837331376017411684046883419847112451557707112313701952475046499434123165306971887183342218577905091225019168102519632392680652950034829050456155599721420172627609282223316200319281946043203041183312672948570622607342759456933199545424994771745683533849070166461271199398599888635697996575023776983811520986333204998150155144593150177881271250692675738287523444924513011607684404183624345099458604527141560605516663126679124591757671374968760476699746532432043029556319210145936709090854515645298082483217416568325348254867513190259004608214401408393290370087999455366477379222523261565770697582600952946677561449929056792243097662976947896070464410947084596785910993183641146463183131781031786749458261667680299065755441772382453069255511591286495843110089827315729875476195687612494038208244555633797003077034781831199181680486599779939313040992140472673212246945388518288324681364787142502502894483205349145682340543862864943079505911592303955582603300381592838583432533882167253481338595830199825225811271374034918946982435485602539618387321781443982253388904741323931270195150576446793714199077491458188570503655185864932068186735720163096928288037450754035810481381537917475420042163153585425212631041547635243494527182"}

Need to prove:
perpendicular(Line(X, Z), Line(Y, Z))

Proof:
