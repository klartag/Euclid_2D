Assumptions:
A, B, C, D, E, F, G: Point
f, g, h, i, j, k, l: Line
distinct(A, B, C, D, E, F, G)
distinct(f, g, h, i, j, k, l)
f == Line(A, B)
g == Line(B, C)
h == parallel_line(C, f)
i == parallel_line(A, g)
D == line_intersection(h, i)
j == internal_angle_bisector(B, C, D)
E == projection(D, j)
k == Line(D, E)
l == external_angle_bisector(B, A, D)
F == line_intersection(f, k)
G == projection(B, l)

Embedding:
C := {"x": "0.7960043912398899745852531850687228143215179443359375", "y": "-1.0340010921032245505557511933147907257080078125"}
B := {"x": "0.968393742435021298575748005532659590244293212890625", "y": "0.8770345483054793334076748578809201717376708984375"}
g := {"point": {"x": "0.968393742435021298575748005532659590244293212890625", "y": "0.8770345483054793334076748578809201717376708984375"}, "direction": {"x": "-0.1723893511951313239904948204639367759227752685546875", "y": "-1.9110356404087038839634260511957108974456787109375"}}
A := {"x": "0.176085851587959696384899643817334435880184173583984375", "y": "0.042665163088739486985101478921933448873460292816162109375"}
i := {"point": {"x": "0.176085851587959696384899643817334435880184173583984375", "y": "0.042665163088739486985101478921933448873460292816162109375"}, "direction": {"x": "-0.1723893511951313239904948204639367759227752685546875", "y": "-1.9110356404087038839634260511957108974456787109375"}}
f := {"point": {"x": "0.176085851587959696384899643817334435880184173583984375", "y": "0.042665163088739486985101478921933448873460292816162109375"}, "direction": {"x": "0.792307890847061602190848361715325154364109039306640625", "y": "0.834369385216739846422573378958986722864210605621337890625"}}
h := {"point": {"x": "0.7960043912398899745852531850687228143215179443359375", "y": "-1.0340010921032245505557511933147907257080078125"}, "direction": {"x": "0.792307890847061602190848361715325154364109039306640625", "y": "0.834369385216739846422573378958986722864210605621337890625"}}
D := {"x": "0.003696500392828372394404823353397659957408905029296875", "y": "-1.868370477319964396978324572273777448572218418121337890625"}
l := {"point": {"x": "0.176085851587959696384899643817334435880184173583984375", "y": "0.042665163088739486985101478921933448873460292816162109375"}, "direction": {"x": "0.77843523864011080718623117469308209634443224027768955557613860104492159175872298684195038044248633530771392621326897118098284314982756929955305930053436134456255916956622430093033245764606175177517475277473082992830398527874505512686825880289698815521246740670174575737079432665215518879586501370877007196349545475296226047112086351036635334006867734648740069406859430568078646437464997756488946923483252576442003584099343468602768169836735693678757890843380842248326229631134428330025989514163921140442338258340034023777085066565874415262498209366611222312654059942360215785202131635498708408085677529422880340723888312925601571994508893683130290702600663991836408016425795508553954323756512805640379413036675844746164927046730849339345769467776528389731415635145919918114371943283937919512514341104690148295840527478973763931091431334661659082676313652108840964643432851820676038982998496073554144787105029982162571838881613689214044431037453595983961417989911706544064846589774851298489222418947736403251703809310979885784766376921923142673851724831810972033436458134673814377826921871059071747466693378835564527156359672322061981689408009968482194575029733266971997539342619373924023584302372187252396925550514231655295317380863108672007718272249831296098257596950571149803894462538535077257123211431420487163101451011252609763992379553026485668144951083160046904357909724621088081674602688399264666563960749772697813320009687383785201393203170268422635528113519787200478966653252252454250461523615880459547614812640168094240341533916603972444665141264747165236530952037709574144919661904194480098234236301475984394461140742888004589851597011760500578468510688609837216597260430805246646307549594062159658088680457407788639926210900950038613275568203521412976491246172376752657552520293624555236815270496639644750394236105578136767266822162841594132033868920228874142557764120047669023010663867236263710058816273129255686499139644938747315714017130894289997416100615253173172161906022668598818164", "y": "1.7211042680992439372575798648785928904446433584412840237569961280556867811148071005772211899327898803096937222430409996013459111187404056182080070826124689280210725689935768994666185027767383458010426821753456257173793863963083761255475830947410505059680091116510498507203717007243333230106167647424621250756726576573799339530633427653569969726125728408421963279221520107103063291645715299931904673413425109174572477468584987837298593831639725355402219114450403449428681574417522375839270084262799343204830278663039974870202051305683647290253780495722135512188156764071070631742716739362293810413758904340249069636629131251803092671435380003922542309500981998955372585060195246145490426426706038917263749016846911441900060025510432816828538587661034704786202986169891489506052644884880925537092155320338620976159217248578665248947005839059305194615692275887757220229024357724717466784901150905954115153807761935661033536201570597856251434635364754622338619427791295746671924126382569461105531555495734096517490400928522887800482036430067149184325739674283586312698019077220338264473130665171008304257334859099036194370994888526710700775781322525998623361119284835007873933978405167999985083839450746337298845294176878287292474195540895934702423145088975228348997967276568234005208534823497912907492570130220863057140268606714526518580771916372038606539368805710978279862926909838712717505073624213819523877635779049040964716385112891554639502386312593841524499018123203821826496091346129494799654733140867654873004871855315048857055644373219506849890983924836126198215456244182132010787601375720863206431264224132535916907652251640296210420035843545194528567721230518706265813752214286786179977879006856617330946080732050021367611975399034414978517577009695977278706358185518231655866758708217911083390106235631095912042394521824221015403078018114236465962149035585934297015178389637262207629371887422694236545621524364765844866135705933099823356754196306264859529968383351842539918971134792600945966"}}
j := {"point": {"x": "0.7960043912398899745852531850687228143215179443359375", "y": "-1.0340010921032245505557511933147907257080078125"}, "direction": {"x": "-0.59875025250090519342859038548722560706197432059943249982100882900651537105054246092055728441656838547818506616496272039801218548570731171525344102976952328420321299731978621623053142895076495030732890091776953219370356485382291819657603666601247820355057456300913007517117667165162459698078377989032488936818138591678962311103593442234798860916041409300345668150770545998043336152089864523125079398675776547715719124727010865715526701383212367506154328886970352250523139355376908958011239471311623993898531460693098567923008954274898380257815788238452722454968864010094720224891834535022532768330630436473044203061251426482610414745038260546426836000195456351945414489981927461425295923229598652187143207683123988303458479417521899834490350882412644744084791190254385937235581595659616715705838943914597597432021622925990635807579984037765643266095191330338412319958238527601374574144863308599389018313065028282798001771457976152162744244226789103170228450757300032069015709608521166948303426224955895816703662048688552962873221288014308619073362818393992892233827554283450707347704794659026008749665155550517190186051149230099246587408476409755465313609338230010187162837554120425207287455277269655088207447284690567570303043369948655759858351750318796827151541789464074507722150619651788925713998547561666225365243384977147631085515492584519759439040253324472653109057448003216284046639157299372357136250224322738737252238158615545873787773889512374203910262165152895309356699232512313575744506476593919751312381363954657012932413328050974335324335129455087306558164581436050499050309374964686584160402053632803212144996744345195197722074012688888227735235828713498143904602971305117798712015115188935813507830987738552934378187626689117997475615750396171185023730767089423137334842673385957309983255654019768277976857339767014850297668872394492176464758719189678819024766506408513244556018780369764225455891217025698981938980013095203793282146746466106695188559166526992553994674397033663820563668", "y": "0.27080770429214502074530679467525776618877691619379115023432917343590864458349737529570383759792281102429110022619402854481277798796224392585575772412506747918841044741374824114258976020055628921864308315211761752938896055285758251885156578681555509941560435364252118538072416946461465648966039863894318774012511999868748966366892061299017821609410699853222854846351080493046569729676901722442902046024102194200942981387240144575054479141130382051731931680202955046684625503219924616949041965469593441722397254591231465987697012809185163672996115459589422662100554657514857965560327030437074818205648027452720177402656349012755358750420684339600394583244882863694058560045866459003201664100466505446457721443939129798787032916280105083261647850424290461208452585582392061376546451964182759967165341682300974514336455492988317714572168146546500209354405672231068848441256555997271108553070287091211490181919025717143346222918198722959224245012679832445501129761749881790844210235456660966453926329048252293562291582293673535076811254308381322846332741848920172739763581984985581333921400939474185133374966795038928573223756709096972472968066246855295448876744669793603039783976879928987522677307329853330116590869682992460425466157120098549386030333545889986019035217245736796983268279155787554654084973469304838392061017437955292892078839345623322703750656470135626932730660184736796757907973602913631110101680528330403105956486070204390634960482817363260208852388345418866222251091224113931485294786629748881632504568446807161367577216530204334466884037681953117574929854065870367091004656080287958668896216092212162985845994039060363023439752259693668847890055720872581797792190783328403435393908176548723333195080408012153343671001703865234648880994183553661601247650049085995743887078430809239177359144560533453294258466789067411776983513331360845930424716467062499363771739447015716907577141447151380220513899617604526130698734711958628041194211850372402760447848355264314090086294847433851921271"}}
E := {"x": "0.45153768522623908878454478403293954106401892641915062032455642588694120938391007491225396457030716402838935343300245186661850258833438140412702557487909308299699367234791591808458954196042025328654659845385589992148516611373589306459291322966321814555011206048108600361373579243573289667496933588031314916211825460530903826002709943920173815893173755424992081499990641284864403012517746123900394818540332554698261007370430227810638666795773872387005488085431703381733643044892697870539666221378083921670903382318276865713470518671390808898010266918392647050933402074285826296803993407451409447241283207595972650790634002231033015835523268412893670042628427178083019908843100792130133062786155060754278921101661914605146005308366543591662238069215022938179549069919792848462764248031808008440170999295547608704665366697194256033621451267265983435170773367140542456786763929406554043724337691087311232718433853136289566799972043029225814296460149878018366309368767676414674866720322545443860360632461787775571566502475960967777872220973717381243134742575885047836452969776033774590519735246467983577536420480840060667820844834725826069054659047209790634758497628851231710170736115629640833626915097600126974629070594404128731136495745787910875188335790584341565121820354208762935269889358527218276927230749848440382961450009808884900993509991572892238458402140953161934318112446646149537093765768854262212224871409486129746569579437230852780806186134514644729295331405066471323820795745272737202406972073633346856602462084922768556592886749967304557710924480485056962727713960396220830268536506896345510893827764450606997352836930116920128674925194118236104702422285215368494267378768960242281133836799769053310046551998983668921929149272371065036112474138823799684429030780058592169170852208030528265503245389552677446070960402807314674982522680757693427950713998616621237254052130610751693562700661691915923325211885166819879000508082864909349733977986083196942232450445822423212866486815975807446239", "y": "-0.87820284822608648710393148680360172213090948805611857724737736589356463988659900105015878122931340733501015134654247635527631804145043140125316281239362887999691406940173435834546751131999348490462604091336244075561801590474512258130864351949014594302658578393374236328952372175290084868516744161969511249839073935338141860909459178301663928962709990705099908022237719828291383486119718956751573688135452528486175955249657216592826409993452855498857159772857199772312175882866097508724388148101109757601868092909017318104149731746673652814202407399696035147766441367389446069967979461501233513635625392036391089515184959836337741888453146504390203635114702006793358146806774129346106763211459378747471320201965526537775765356766954597772086369369847348328839626501045778149725740082296648973897333867608778966150092752723853588941792004090629052513573111824172387693223814593285822950494849597759948589129191958302428007774728043070654295757530222136670794613115027235972215211415500175001765820626585486919585274704604565147417255331405519880303345166947146725602719556140249909909188146979132605197156205619441944186734025288737007102999421128088954907598841882233543750662742126989663328178717465094374454918500260765063550058796777617090874648052578422765475129930100077345044692304923368103901511558368701471139389913829278170324322458961318712630446176427225106134666237340857104528900786136670869071402995475617822768957570753651067105224608426294110103987721179902217479090950571006245009183930894768884015259838191813462436723679690067451593104863741127203003541124930188877918683859683561860240899588253098542087476520200680531640052477184514571539903875327504382703641573280319658351399019661666440124217159065187545976415376247327905343499618721116050220729590287466666594575941441586332064012387667616176637888049061546159594359953352302752138787329837971337723913481046691343365442141368853500214880237644379579355595649789197219800472840687879354145685738567632107341326444711381854694"}
k := {"point": {"x": "0.003696500392828372394404823353397659957408905029296875", "y": "-1.868370477319964396978324572273777448572218418121337890625"}, "direction": {"x": "0.44784118483341071639013996067954188110661002138985374532455642588694120938391007491225396457030716402838935343300245186661850258833438140412702557487909308299699367234791591808458954196042025328654659845385589992148516611373589306459291322966321814555011206048108600361373579243573289667496933588031314916211825460530903826002709943920173815893173755424992081499990641284864403012517746123900394818540332554698261007370430227810638666795773872387005488085431703381733643044892697870539666221378083921670903382318276865713470518671390808898010266918392647050933402074285826296803993407451409447241283207595972650790634002231033015835523268412893670042628427178083019908843100792130133062786155060754278921101661914605146005308366543591662238069215022938179549069919792848462764248031808008440170999295547608704665366697194256033621451267265983435170773367140542456786763929406554043724337691087311232718433853136289566799972043029225814296460149878018366309368767676414674866720322545443860360632461787775571566502475960967777872220973717381243134742575885047836452969776033774590519735246467983577536420480840060667820844834725826069054659047209790634758497628851231710170736115629640833626915097600126974629070594404128731136495745787910875188335790584341565121820354208762935269889358527218276927230749848440382961450009808884900993509991572892238458402140953161934318112446646149537093765768854262212224871409486129746569579437230852780806186134514644729295331405066471323820795745272737202406972073633346856602462084922768556592886749967304557710924480485056962727713960396220830268536506896345510893827764450606997352836930116920128674925194118236104702422285215368494267378768960242281133836799769053310046551998983668921929149272371065036112474138823799684429030780058592169170852208030528265503245389552677446070960402807314674982522680757693427950713998616621237254052130610751693562700661691915923325211885166819879000508082864909349733977986083196942232450445822423212866486815975807446239", "y": "0.99016762909387790987439308547017572644130893006521931337762263410643536011340099894984121877068659266498984865345752364472368195854956859874683718760637112000308593059826564165453248868000651509537395908663755924438198409525487741869135648050985405697341421606625763671047627824709915131483255838030488750160926064661858139090540821698336071037290009294900091977762280171708616513880281043248426311864547471513824044750342783407173590006547144501142840227142800227687824117133902491275611851898890242398131907090982681895850268253326347185797592600303964852233558632610553930032020538498766486364374607963608910484815040163662258111546853495609796364885297993206641853193225870653893236788540621252528679798034473462224234643233045402227913630630152651671160373498954221850274259917703351026102666132391221033849907247276146411058207995909370947486426888175827612306776185406714177049505150402240051410870808041697571992225271956929345704242469777863329205386884972764027784788584499824998234179373414513080414725295395434852582744668594480119696654833052853274397280443859750090090811853020867394802843794380558055813265974711262992897000578871911045092401158117766456249337257873010336671821282534905625545081499739234936449941203222382909125351947421577234524870069899922654955307695076631896098488441631298528860610086170721829675677541038681287369553823572774893865333762659142895471099213863329130928597004524382177231042429246348932894775391573705889896012278820097782520909049428993754990816069105231115984740161808186537563276320309932548406895136258872796996458875069811122081316140316438139759100411746901457912523479799319468359947522815485428460096124672495617296358426719680341648600980338333559875782840934812454023584623752672094656500381278883949779270409712533333405424058558413667935987612332383823362111950938453840405640046647697247861212670162028662276086518953308656634557858631146499785119762355620420644404350210802780199527159312120645854314261432367892658673555288618145306"}}
G := {"x": "0.62392703642137041277503960449687631698679419497383812032455642588694120938391007491225396457030716402838935343300245186661850258833438140412702557487909308299699367234791591808458954196042025328654659845385589992148516611373589306459291322966321814555011206048108600361373579243573289667496933588031314916211825460530903826002709943920173815893173755424992081499990641284864403012517746123900394818540332554698261007370430227810638666795773872387005488085431703381733643044892697870539666221378083921670903382318276865713470518671390808898010266918392647050933402074285826296803993407451409447241283207595972650790634002231033015835523268412893670042628427178083019908843100792130133062786155060754278921101661914605146005308366543591662238069215022938179549069919792848462764248031808008440170999295547608704665366697194256033621451267265983435170773367140542456786763929406554043724337691087311232718433853136289566799972043029225814296460149878018366309368767676414674866720322545443860360632461787775571566502475960967777872220973717381243134742575885047836452969776033774590519735246467983577536420480840060667820844834725826069054659047209790634758497628851231710170736115629640833626915097600126974629070594404128731136495745787910875188335790584341565121820354208762935269889358527218276927230749848440382961450009808884900993509991572892238458402140953161934318112446646149537093765768854262212224871409486129746569579437230852780806186134514644729295331405066471323820795745272737202406972073633346856602462084922768556592886749967304557710924480485056962727713960396220830268536506896345510893827764450606997352836930116920128674925194118236104702422285215368494267378768960242281133836799769053310046551998983668921929149272371065036112474138823799684429030780058592169170852208030528265503245389552677446070960402807314674982522680757693427950713998616621237254052130610751693562700661691915923325211885166819879000508082864909349733977986083196942232450445822423212866486815975807446242", "y": "1.0328327921826173968594945643921091753147692228813814227526226341064353601134009989498412187706865926649898486534575236447236819585495685987468371876063711200030859305982656416545324886800065150953739590866375592443819840952548774186913564805098540569734142160662576367104762782470991513148325583803048875016092606466185813909054082169833607103729000929490009197776228017170861651388028104324842631186454747151382404475034278340717359000654714450114284022714280022768782411713390249127561185189889024239813190709098268189585026825332634718579759260030396485223355863261055393003202053849876648636437460796360891048481504016366225811154685349560979636488529799320664185319322587065389323678854062125252867979803447346222423464323304540222791363063015265167116037349895422185027425991770335102610266613239122103384990724727614641105820799590937094748642688817582761230677618540671417704950515040224005141087080804169757199222527195692934570424246977786332920538688497276402778478858449982499823417937341451308041472529539543485258274466859448011969665483305285327439728044385975009009081185302086739480284379438055805581326597471126299289700057887191104509240115811776645624933725787301033667182128253490562554508149973923493644994120322238290912535194742157723452487006989992265495530769507663189609848844163129852886061008617072182967567754103868128736955382357277489386533376265914289547109921386332913092859700452438217723104242924634893289477539157370588989601227882009778252090904942899375499081606910523111598474016180818653756327632030993254840689513625887279699645887506981112208131614031643813975910041174690145791252347979931946835994752281548542846009612467249561729635842671968034164860098033833355987578284093481245402358462375267209465650038127888394977927040971253333340542405855841366793598761233238382336211195093845384040564004664769724786121267016202866227608651895330865663455785863114649978511976235562042064440435021080278019952715931212064585431426143236789265867355528861814530"}
F := {"x": "1.4973543581799352368158269513654876325983186562196862608036973928181757425054178132919705125530081534701454013328406125273931118555150325091321218150750070369072229640987340240682282406896465571219288058087799135466575248537599372972581234775927947031010487852011147273416846755487156637668225711631837498037812949421622522891629457366628750200544419541812786711342895139999901672408486378395071516124658565983256789004273685211447800745193784490265434791478007281356269860028680579189207519795129538148165585847987345503024977896842971267793152285239061280863287960789983581513920955989042198041451457973258554386162674871269257804788558841481933643649502960988584030526454108904264512132383438673866150296340984454779128653336728671887308516569000755361616639326769096505014046711460501373165889827709087687546209759582673153337876179954570759364518660692886221978030604760427479702836088464132238603244295678630640170440344970974545363551828748941018563933182885745531551070899502250183249810777839460997042481497301101764154224198796535839055915069208816912341707223671345419869829249833933314565961737768512080088612280095141521374837226107637523388258746012835661874007467536461088653504045290017024628042155126975095996707505454596381638053931542902981550413541455162867251655496202103606754133151541522200033101190968798302090224822120029614945400859449430694249894738961935478771438417767696512794841486627326758734542939079861444244852557159001165768055766993587634904954835094339914824848073238123434364310523194196916735994159975800306703449808392716658470411474979781605019896407889542623095097978724106015696342935330619076291494867314728105594706188174568262475845440618859074078777759141346334703591936558987775660320900870568687231040046107630748530984596274492104494622761007805183957323960347820112196327626234054505775536557760833248647317337705955613310114740512781623292004425852310841598755257067709753617586759650888303697720243189585711604151350241279158285639198010017101310", "y": "1.4340762600712215088289278703254433289206616778944069641896352182041192793297966820844095105488247831845308295156195763547828754926717208588725425953663389916491858904050947730947430439012498554782273904308994479685707775261330080567968830237007496944261141124296548675691855919069330959689876526456908247852325544826796983993855663698224757216694385971936270024413701250049587036014079783673808024689463938205380395720834867448352056749972077171574752721649545974464979836808393555242731292996575848462825610252628416862198485802306237046598764014679832111094869548389641711430384266798495380844208968648815743056422344274878244838972888777268275035251233534534415178423233831327488650474406689854747943185724157620796767040825457734156098582095091019087983735622762226468983840287638055405751258326790613317481193244143491587077752633992013705533287283501734295612711250530547848386531592625011073172847414193588022858767555442184510098486300869186064881660988086935560922100764529828404398161239755835539006053384172955683772252466736373887988987061373179571540440702225800369091903088277384085448573464922672305519841586287676451499487260418935700690363535221831644296113092094368557592601821348241080787973747045513249311552255817389244668021587019212429836887298500524680386075730037271971012281093377136464280049303063101946445948801875261968084273667743959275741984636511397544471081393049628292826327948709526146129929165709441961274374918708552308292019405263205679173136563205298449892126220169877082826314181678347873943090656861275939981762384583302197221140585048139276630522790793136986149054236634754250802857538940251218302737481157071499372068474519408335951323552857108293647780083598851640040669916964975738924714676235508233667031688875327988483748669786558779349374830888097934010882806927005969598934695093352685191555618604786684963881971025136905158024848520900208752171779820751726548215206851331742898200003957664607429496024711197609270957156825387935924414926117179734242"}

Need to prove:
concyclic(A, E, F, G)

Proof:
