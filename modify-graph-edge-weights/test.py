import unittest
import big_input

from modify_graph_edge_weights import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        n = big_input.n
        edges = big_input.edges
        source = big_input.source
        destination = big_input.destination
        target = big_input.target
        result = s.modifiedGraphEdges(n, edges, source, destination, target)
        self.assertEqual([], result)

    def test_4(self):
        s = Solution()
        n = 5
        edges = [[0,2,5],[2,1,-1],[2,4,3],[3,4,5],[4,0,1],[0,3,-1],[2,3,-1]]
        source = 0
        destination = 1
        target = 9
        result = s.modifiedGraphEdges(n, edges, source, destination, target)
        self.assertNotEqual([], result)

    def test_0(self):
        s = Solution()
        n = 5
        edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
        source = 0
        destination = 1
        target = 5
        result = s.modifiedGraphEdges(n, edges, source, destination, target)
        self.assertEqual([[4,1,1],[2,0,1],[0,3,3],[4,3,1]], result)

    def test_2(self):
        s = Solution()
        n = 3
        edges = [[0,1,-1],[0,2,5]]
        source = 0
        destination = 2
        target = 6
        result = s.modifiedGraphEdges(n, edges, source, destination, target)
        self.assertEqual([], result)

    def test_3(self):
        s = Solution()
        n = 4
        edges = [[0,1,-1],[1,2,-1],[3,1,-1],[3,0,2],[0,2,5]]
        source = 2
        destination = 3
        target = 8
        result = s.modifiedGraphEdges(n, edges, source, destination, target)
        self.assertEqual([], result)

    def test_5(self):
        s = Solution()
        n = 5
        edges = [[3,0,1],[2,1,-1],[2,3,6],[4,2,6],[1,3,2],[2,0,7],[0,4,10],[0,1,6]]
        source = 1
        destination = 4
        target = 14
        result = s.modifiedGraphEdges(n, edges, source, destination, target)
        self.assertEqual([], result)

    def test_6(self):
        s = Solution()
        n = 100
        edges = [[0,70,-1],[10,25,-1],[12,5,-1],[5,20,-1],[55,13,-1],[14,33,-1],[63,16,-1],[43,18,-1],[19,87,-1],[26,21,-1],[51,31,-1],[88,32,-1],[35,44,-1],[36,39,-1],[3,37,-1],[3,11,-1],[11,34,-1],[46,34,-1],[88,40,-1],[72,45,-1],[47,28,-1],[28,93,-1],[49,57,-1],[30,51,-1],[30,42,-1],[52,4,-1],[87,53,-1],[55,9,-1],[56,87,-1],[22,58,-1],[29,22,-1],[9,60,-1],[9,25,-1],[61,7,-1],[24,62,-1],[24,67,-1],[67,73,-1],[69,68,-1],[23,69,-1],[23,46,-1],[1,71,-1],[1,80,-1],[2,72,-1],[39,2,-1],[70,39,-1],[63,70,-1],[57,63,-1],[57,17,-1],[26,17,-1],[26,94,-1],[96,73,-1],[74,29,-1],[75,46,-1],[15,46,-1],[82,76,-1],[59,77,-1],[59,8,-1],[38,8,-1],[33,38,-1],[33,7,-1],[93,7,-1],[41,79,-1],[41,97,-1],[90,80,-1],[82,27,-1],[27,84,-1],[48,27,-1],[48,20,-1],[20,50,-1],[65,85,-1],[86,43,-1],[66,43,-1],[66,87,-1],[87,78,-1],[54,78,-1],[94,89,-1],[98,92,-1],[6,93,-1],[6,65,-1],[65,44,-1],[4,44,-1],[88,4,-1],[88,99,-1],[98,94,-1],[95,25,-1],[25,64,-1],[64,15,-1],[83,15,-1],[83,91,-1],[91,42,-1],[42,54,-1],[54,90,-1],[96,50,-1],[90,50,-1],[81,90,-1],[81,29,-1],[29,97,-1],[97,99,-1],[99,98,-1],[41,68,-1],[5,16,-1],[81,68,-1],[96,20,-1],[5,77,-1],[63,78,-1],[92,56,-1],[75,96,-1],[55,44,-1],[86,25,-1],[27,79,-1],[46,94,-1],[45,14,-1],[96,36,-1],[88,9,-1],[60,43,-1],[82,45,-1],[33,41,-1],[12,56,-1],[10,46,-1],[79,40,-1],[20,63,-1],[79,9,-1],[77,63,-1],[22,64,-1],[22,57,-1],[44,82,-1],[69,9,-1],[80,0,-1],[36,62,-1],[25,84,-1],[73,21,-1],[22,74,-1],[57,24,-1],[57,82,-1],[98,85,-1],[36,74,-1],[77,48,-1],[72,11,-1],[35,62,-1],[22,94,-1],[96,35,-1],[85,51,-1],[19,59,-1],[24,17,-1],[42,61,-1],[5,87,-1],[91,90,-1],[49,15,-1],[26,84,-1],[79,22,-1],[44,6,-1],[84,64,-1],[20,52,-1],[50,88,-1],[89,81,-1],[12,22,-1],[7,21,-1],[54,52,-1],[78,12,-1],[31,39,-1],[75,55,-1],[57,15,-1],[34,84,-1],[85,88,-1],[86,2,-1],[34,31,-1],[17,96,-1],[82,69,-1],[73,6,-1],[21,22,-1],[29,48,-1],[81,83,-1],[66,79,-1],[18,46,-1],[25,63,-1],[75,83,-1],[88,36,-1],[90,53,-1],[81,12,-1],[76,97,-1],[44,18,-1],[63,12,-1],[68,5,-1],[43,22,-1],[21,37,-1],[63,42,-1],[50,83,-1],[87,41,-1],[24,33,-1],[95,76,-1],[33,28,-1],[60,42,-1],[33,18,-1],[73,70,-1],[12,90,-1],[97,15,-1],[96,86,-1],[69,77,-1],[10,78,-1],[16,85,-1],[35,56,-1],[78,14,-1],[92,50,-1],[18,15,-1],[65,47,-1],[91,16,-1],[66,3,-1],[19,22,-1],[23,95,-1],[97,48,-1],[83,25,-1],[47,71,-1],[77,54,-1],[74,98,-1],[89,48,-1],[25,0,-1],[7,71,-1],[46,38,-1],[43,38,-1],[3,78,-1],[81,36,-1],[91,65,-1],[74,83,-1],[46,77,-1],[72,92,-1],[10,69,-1],[94,77,-1],[79,44,-1],[85,84,-1],[20,41,-1],[1,60,-1],[37,74,-1],[6,53,-1],[31,20,-1],[27,81,-1],[49,10,-1],[86,32,-1],[15,90,-1],[55,12,-1],[79,99,-1],[99,71,-1],[53,3,-1],[32,62,-1],[49,78,-1],[47,36,-1],[5,6,-1],[50,36,-1],[87,21,-1],[17,31,-1],[3,98,-1],[8,83,-1],[30,3,-1],[87,67,-1],[22,91,-1],[9,46,-1],[70,18,-1],[82,75,-1],[14,93,-1],[93,64,-1],[60,64,-1],[4,35,-1],[95,57,-1],[23,24,-1],[60,47,-1],[23,36,-1],[28,44,-1],[25,20,-1],[20,47,-1],[27,95,-1],[81,64,-1],[51,61,-1],[15,3,-1],[9,7,-1],[34,6,-1],[9,96,-1],[22,87,-1],[0,71,-1],[31,96,-1],[29,16,-1],[82,80,-1],[99,70,-1],[63,89,-1],[10,91,-1],[26,85,-1],[59,93,-1],[71,10,-1],[69,15,-1],[39,62,-1],[5,13,-1],[9,10,-1],[98,97,-1],[48,30,-1],[27,35,-1],[11,68,-1],[70,4,-1],[72,77,-1],[81,0,-1],[2,59,-1],[17,75,-1],[53,19,-1],[99,82,-1],[11,75,-1],[99,6,-1],[36,66,-1],[31,10,-1],[35,67,-1],[41,15,-1],[18,26,-1],[17,40,-1],[50,3,-1],[81,79,-1],[75,2,-1],[40,24,-1],[34,77,-1],[35,38,-1],[90,8,-1],[40,38,-1],[55,5,-1],[37,58,-1],[16,50,546959],[59,56,-1],[71,27,-1],[55,86,-1],[25,34,-1],[85,91,-1],[93,1,-1],[54,12,-1],[43,6,-1],[49,18,-1],[76,62,-1],[56,30,-1],[23,15,-1],[60,28,-1],[50,48,-1],[58,81,-1],[19,74,-1],[52,91,-1],[3,60,-1],[0,82,-1],[1,26,-1],[75,39,-1],[88,93,-1],[54,33,-1],[15,60,-1],[48,25,-1],[44,43,-1],[52,75,-1],[68,80,-1],[11,12,-1],[67,75,-1],[15,99,-1],[37,46,-1],[1,9,-1],[94,47,-1],[20,53,-1],[44,23,-1],[31,0,-1],[63,32,-1],[32,16,339080],[32,50,-1],[25,60,-1],[46,33,-1],[58,39,-1],[25,74,-1],[16,20,-1],[39,8,-1],[73,7,-1],[23,80,-1],[36,25,-1],[69,86,-1],[33,43,-1],[4,92,-1],[70,29,-1],[1,32,614157],[58,31,-1],[42,52,-1],[12,77,-1],[34,64,-1],[77,92,-1],[43,51,-1],[51,42,-1],[7,12,-1],[53,9,-1],[11,42,-1],[13,60,-1],[85,12,-1],[56,90,-1],[39,61,-1],[78,89,-1],[43,95,-1],[23,31,-1],[77,60,-1],[66,26,-1],[52,70,-1],[50,71,-1],[23,38,-1],[25,2,-1],[52,95,-1],[36,30,-1],[2,36,-1],[32,83,-1],[20,95,-1],[81,65,-1],[94,6,-1],[80,6,-1],[22,17,-1],[3,52,-1],[31,38,-1],[6,32,-1],[56,29,-1],[97,11,-1],[89,55,-1],[56,49,-1],[39,85,-1],[66,83,-1],[59,22,-1],[89,69,-1],[95,47,-1],[12,25,-1],[10,28,-1],[25,71,-1],[31,98,-1],[13,46,-1],[93,69,-1],[81,99,-1],[30,16,-1],[3,28,-1],[87,82,-1],[87,57,-1],[47,32,-1],[94,7,-1],[78,40,-1],[21,48,-1],[19,47,-1],[59,50,-1],[29,49,-1],[47,18,-1],[98,19,-1],[33,83,-1],[61,5,-1],[93,41,-1],[47,46,-1],[41,95,-1],[32,12,-1],[44,69,-1],[38,72,-1],[59,7,-1],[78,33,-1],[99,73,-1],[41,49,-1],[76,46,-1],[69,35,-1],[3,77,-1],[3,69,-1],[58,47,-1],[88,90,-1],[15,78,-1],[68,76,-1],[27,59,-1],[0,77,-1],[83,63,-1],[42,72,-1],[96,7,-1],[48,39,-1],[23,30,-1],[38,34,-1],[10,35,-1],[38,74,-1],[18,6,-1],[89,65,-1],[19,66,-1],[6,10,-1],[46,78,-1],[98,7,-1],[82,40,-1],[99,32,-1],[60,63,-1],[63,8,-1],[20,92,-1],[7,30,-1],[31,66,8298038],[58,45,1852958],[28,51,1537858],[11,79,1907154],[4,23,9938233],[61,92,4483031],[12,62,5714570],[99,1,2726140],[5,40,7911717],[32,54,728475],[85,49,5515899],[32,51,4978970],[6,90,5121669],[63,41,8629904],[77,78,4631691],[81,6,7724808],[41,91,7133902],[68,32,2096045],[12,76,3212150],[99,8,9337750],[50,2,291794],[97,21,9004592],[68,4,9972157],[8,64,3096621],[2,88,3221326],[78,82,3360712],[90,45,5711931],[55,34,4337975],[89,74,8837978],[93,76,3476696],[49,79,6751928],[96,32,8036427],[87,96,2555030],[84,86,4824524],[59,10,9765354],[75,57,7450247],[67,16,8140905],[79,32,7646192],[32,90,1805238],[51,94,7825217],[61,76,6549674],[0,49,4047564],[67,76,7502276],[65,35,4158012],[39,66,2936020],[71,91,3675514],[16,14,7638840],[33,8,8316745],[58,20,5690887],[36,11,1925080],[56,18,2109216],[11,37,6601594],[62,7,2349594],[34,70,335659],[64,73,3532223],[69,14,8366677],[93,62,3496504],[86,60,6853618],[40,33,7387004],[64,6,9812066],[21,63,1565219],[81,85,9685719],[80,27,9446711],[68,23,6644184],[9,18,8684884],[6,56,6714111],[66,69,7557406],[14,5,2047520],[35,11,5902488],[62,63,1626998],[24,9,2411504],[97,35,398149],[45,98,7259164],[68,49,5947610],[62,2,940435],[4,22,6646542],[94,69,5596779],[80,49,6807023],[6,37,304172],[79,59,1502937],[35,89,7126557],[89,11,8821391],[63,97,1620748],[73,48,2918685],[7,11,3547869],[41,16,8650491],[0,54,2311100],[49,31,7430358],[91,84,659913],[74,24,7522373],[69,40,4887014],[63,2,2659548],[35,41,2943705],[50,49,7133684],[76,23,4051856],[64,18,8912356],[24,0,3261023],[26,9,9909037],[4,50,3969627],[20,71,5871486],[95,28,7179630],[42,86,4604324],[16,95,8633058],[48,98,4867290],[66,63,8803607],[59,6,6807917],[52,82,1219440],[73,46,9386714],[67,51,5179108],[8,47,1815185],[65,96,3768552],[95,56,8976525],[5,90,1031684],[86,22,9016224],[25,43,9578559],[84,83,1223918],[39,77,5086761],[21,58,59721],[1,62,2867766],[55,74,3194478],[81,93,5537508],[26,89,9617063],[12,53,4561903],[74,54,2966417],[96,43,5026329],[49,36,7683124],[89,44,1777180],[73,75,9195851],[93,83,4789077],[9,37,6599750],[66,77,2764102],[96,82,6949551],[11,39,2328228],[74,92,5799729],[24,26,9206230],[35,59,2525909],[22,42,3879398],[50,35,3584691],[51,18,2102900],[36,77,2095100],[91,6,6509103],[89,19,4107575],[27,51,3165220],[30,2,838234],[86,87,7963038],[87,15,7403777],[0,6,5206608],[3,38,9188085],[53,69,7142400],[4,53,5516702],[23,92,703495],[7,66,9136959],[71,54,9472839],[12,59,9960051],[28,2,4344741],[44,99,7224317],[2,67,6312388],[63,86,4280713],[37,34,6824932],[36,42,2991374],[45,44,4947837],[73,13,3717717],[15,96,8841401],[94,16,3606955],[60,7,8512802],[95,98,2666226],[9,21,1258187],[9,63,1730576],[87,64,8451700],[90,30,3835581],[51,52,4203913],[82,28,348982],[75,9,8464685],[67,69,6722826],[84,88,9035830],[62,70,1399995],[45,85,8615860],[46,57,6613076],[1,21,1029524],[70,54,6026341],[24,8,7314172],[54,41,2295308],[84,54,5047012],[31,63,4498624],[22,51,6311791],[48,22,4603127],[2,92,25872],[68,86,8921225],[64,39,1252626],[58,8,7882154],[36,68,144359],[18,13,8539432],[0,56,4665355],[93,13,535786],[1,84,140957],[26,86,6045595],[49,61,2720143],[75,30,3962653],[77,56,7826981],[36,46,2889756],[47,30,5326484],[30,60,8373737],[37,65,620225],[56,84,1830006],[5,66,7260286],[37,91,3483235],[21,34,3927719],[56,67,6350833],[90,35,3614541],[47,76,1123895],[6,14,4645853],[63,81,6612584],[34,52,1342299],[58,7,3842854],[16,47,3756046],[56,65,2041907],[47,67,6322757],[91,48,3620648],[16,23,1679051],[21,85,6237847],[35,20,7786505],[7,39,7278066],[73,84,2411734],[20,82,398965],[63,4,8830240],[56,7,5817206],[43,32,8874197],[20,21,2757971],[42,88,5749813],[24,71,6065909],[78,38,8365528],[78,20,1657223],[58,93,89857],[0,8,5669028],[8,37,1903654],[94,81,6475068],[34,16,4893550],[17,53,3039237],[5,46,4632090],[72,82,6829347],[23,14,3697086],[89,30,6412244],[39,87,2690759],[50,7,1614650],[80,62,537405],[21,91,2315179],[35,68,4927699],[10,98,6286739],[49,59,988578],[41,88,9218615],[12,18,1064906],[16,57,2245112],[15,70,5197939],[17,44,495799],[69,2,2224780],[89,53,4667206],[84,87,8115651],[82,48,7549180],[43,29,9689138],[6,97,1929944],[23,85,4237910],[1,22,5956180],[49,46,474378],[48,3,5184844],[22,72,816179],[98,47,5132634],[27,7,4448224],[49,82,693220],[91,25,6741051],[76,42,5424020],[42,13,4603724],[65,34,3482048],[25,30,5733284],[0,79,8742130],[97,54,487616],[97,37,641195],[86,50,8977633],[78,48,6063351],[57,33,2302206],[71,90,6187892],[29,7,2434416],[45,11,1045716],[99,7,6001560],[54,36,4716642],[11,43,8938058],[53,59,7204356],[17,23,3400434],[45,60,8512827],[32,42,7683523],[18,54,5580447],[85,2,1816428],[62,88,7813939],[14,32,6556514],[82,8,261742],[11,70,7095313],[19,80,3890636],[61,60,952390],[56,68,6258831],[56,66,6504993],[31,79,8776422],[14,42,3290466],[66,11,5267572],[59,63,6061399],[75,26,6851882],[50,58,9922432],[82,66,896401],[30,17,7575715],[70,95,8731457],[88,22,7874162],[36,41,5810850],[72,69,4427463],[62,16,4212615],[8,70,2026928],[64,46,5804066],[95,13,5025452],[8,65,8925599],[35,71,1663097],[14,17,3562587],[46,50,3380712],[10,54,1698594],[59,44,6231117],[55,46,4836197],[57,98,9036062],[34,40,6792602],[63,90,5427244],[72,68,2668961],[62,61,4164705],[16,31,3473401],[30,66,9490116],[86,53,1408975],[46,41,230419],[61,83,9587805],[52,78,1150440],[31,53,1417673],[18,71,5983594],[2,14,6334219],[65,74,8396727],[2,65,2781726],[13,44,1062688],[44,14,7625536],[44,86,3746947],[17,11,3721264],[78,81,4399921],[19,96,6228902],[73,86,3764612],[6,22,7083034],[61,89,9450649],[80,9,7821292],[31,36,6124480],[3,97,9833959],[93,53,1062258],[20,91,1844715],[29,60,764807],[17,66,1115586],[77,99,990795],[38,70,243353],[27,68,7315501],[18,83,5464295],[3,22,2506386],[2,15,7701741],[35,94,2882832],[33,94,4121223],[22,52,4168942],[44,27,2060018],[27,18,1390342],[39,12,7728372],[66,50,9830937],[71,31,851229],[1,59,6358698],[73,90,6518482],[27,77,299586],[50,72,2200156],[92,63,3999049],[8,36,5191754],[92,65,6081757],[64,94,8692009],[98,59,2686755],[16,61,9210049],[62,53,8033016],[19,25,9134462],[80,51,1109103],[52,39,4938780],[76,99,3290507],[79,20,8070907],[65,11,1825262],[29,31,7265613],[67,19,4309781],[13,14,9136113],[31,43,3698673],[12,83,6132878],[34,68,2749169],[44,83,7871771],[13,58,288648],[82,4,6199757],[69,18,758324],[99,59,2359627],[5,24,328903],[27,78,9420271],[98,70,3228525],[6,76,9877260],[47,79,5530827],[29,98,7442119],[0,19,6248310],[57,32,8464719],[54,8,7674398],[20,7,9571533],[54,88,7109717],[58,90,8234996],[39,93,6133608],[84,24,5903100],[45,4,9879292],[17,95,1374897],[23,78,1351225],[33,68,2522648],[30,84,3105994],[58,23,2243253],[1,79,3331040],[49,30,7116601],[24,92,1622663],[44,41,1096718],[11,47,4391717],[0,43,8203893],[77,41,5942998],[2,83,4218888],[50,12,7853108],[57,84,435436],[98,60,9496479],[17,97,4939930],[49,63,9544768],[67,82,1662223],[54,17,6966926],[7,46,3401831],[82,90,6254506],[13,99,8800404],[36,89,7695131],[83,85,6645442],[73,68,4868113],[24,48,2347085],[90,75,9504126],[67,32,630462],[62,44,8279993],[53,91,8696663],[20,43,6258384],[22,71,8688014],[80,65,8377888],[11,41,4738542],[27,99,9819240],[35,74,7615076],[2,70,1540145],[42,8,1729600],[24,54,4564946],[78,11,7028973],[49,90,3360720],[51,62,4175056],[89,17,5405816],[93,90,4777406],[5,15,5493945],[27,15,9006031],[76,59,686718],[50,34,2889465],[41,56,5803388],[25,45,6477235],[52,30,6796587],[72,52,5870111],[57,2,4531309],[92,83,4706455],[28,59,2149931],[68,53,2012941],[38,73,8346254],[49,20,7701335],[1,51,2263864],[1,77,5414424],[90,98,2077319],[43,97,8261900],[40,9,7156544],[32,22,4176073],[37,84,9251965],[36,27,5492951],[34,36,9925486],[6,60,4460578],[72,94,2230737],[57,62,8070015],[93,49,8288373],[91,49,7800970],[50,39,2464860],[50,28,7748241],[55,88,38370],[63,29,5637702],[50,87,4673062],[70,81,258665],[69,81,1895413],[17,46,520253],[50,78,1308210],[65,13,7848118],[99,28,3343490],[1,33,9817646],[72,34,5869695],[70,79,8845305],[84,67,940477],[9,70,7826896],[43,70,8910094],[59,61,1846841],[79,54,6740228],[53,64,1199845],[32,7,3566933],[86,99,5356135],[65,95,3087938],[64,16,9366373],[48,36,2823245],[28,43,1000885],[19,45,9879764],[78,47,15015],[62,14,6273600],[65,98,1436695],[40,91,5308658],[43,56,2651034],[50,44,7634572],[57,85,1922904],[67,93,9009347],[63,55,4970219],[47,25,8325946],[90,65,6951393],[52,65,9784957],[10,45,3777935],[21,79,6869658],[76,55,2545589],[19,54,2716551],[30,44,2004631],[60,57,8799204],[92,46,5078422],[38,2,1726365],[49,69,7323225],[82,29,1904068],[89,23,4403992],[79,6,4679797],[85,0,2992807],[11,5,2022971],[81,91,2041702],[70,32,8691467],[78,31,4222687],[13,77,7721340],[71,98,8387621],[28,1,787126],[17,79,3756957],[25,39,5279936],[86,39,8932673],[9,19,9365443],[47,10,5703596],[55,33,1607695],[37,68,8376275],[18,77,4006134],[70,75,2911815],[73,62,1598040],[13,90,5241001],[77,64,6002852],[8,92,5308276],[28,24,4327149],[80,30,2251444],[36,82,8992096],[33,80,286288],[27,70,3877829],[75,47,6984300],[85,19,9567231],[23,74,2125629],[15,13,1236702],[5,67,8027383],[19,2,4994539],[67,91,383270],[64,14,6145044],[85,8,3478624],[88,20,3495124],[4,13,682799],[39,46,5757726],[36,35,4082149],[34,69,4457775],[10,79,4334754],[80,61,6654667],[17,5,4058481],[83,95,1145041],[46,89,3350279],[5,85,3950561],[20,2,3610548],[81,40,2849576],[34,47,4724649],[68,28,8393518],[90,20,8366659],[45,75,4063931],[93,42,209192],[45,13,5765452],[68,85,8928506],[99,40,5782410],[41,2,9726173],[82,59,3877051],[60,91,2581321],[21,94,7439216],[62,75,9876059],[35,75,5766329],[88,74,8582704],[48,16,9304534],[15,52,8043795],[58,16,8062704],[55,40,6497298],[81,7,6432347],[67,62,2020289],[81,52,4266861],[73,24,6754814],[92,93,4881764],[92,7,4785112],[1,6,8571753],[55,77,6835422],[80,64,6840200],[10,97,7400031],[27,89,6433052],[45,55,8783290],[80,26,902040],[39,42,3881192],[44,31,8810627],[4,56,1957212],[10,15,4014692],[29,38,5425401],[21,64,1821037],[84,92,5565615],[20,51,846982],[62,43,5925179],[16,4,2416033],[85,89,2426036],[7,41,6680023],[47,0,770109],[10,65,313200],[45,94,2678103],[83,59,355355],[37,55,8030162],[46,35,2431164],[76,54,7919919],[93,22,654889],[61,75,4678974],[92,62,1498485],[63,11,1804354],[86,41,1503810],[65,36,3108980],[30,83,315591],[49,84,897060],[5,50,2942151],[78,68,1957444],[2,54,2208605],[89,7,8440376],[53,35,6932928],[43,57,35113],[8,26,7250804],[25,99,9988974],[39,98,5459341],[9,90,8393129],[67,64,6089186],[43,98,8024077],[64,28,685504],[99,96,2293310],[85,74,624835],[70,69,5278684],[32,91,2731439],[21,67,1981617],[42,73,2811714],[13,8,382593],[56,53,4954841],[13,32,6448137],[79,48,1862032],[95,10,4919618],[9,86,810444],[15,76,1641113],[94,40,831146],[0,48,4476704],[96,67,9127247],[33,22,3152508],[93,96,8272282],[96,47,9409949],[78,62,8428417],[71,57,5395234],[20,80,8857948],[37,41,2639729],[56,73,8372015],[2,5,3765590],[22,96,8684890],[13,12,1879593],[97,5,43591],[67,28,2696070],[96,77,4432508],[59,5,4969472],[71,38,1006849],[5,28,7140293],[72,26,5739889],[11,6,8230649],[80,95,666171],[24,81,2742774],[77,14,4642884],[83,37,9892972],[58,42,4095406],[71,15,2854207],[76,2,5511360],[58,33,6307084],[47,59,9345628],[82,41,8168148],[7,82,1253487],[97,12,6448812],[14,76,6319705],[76,49,9253385],[85,36,9864129],[25,11,2506502],[97,36,3849633],[44,36,4956289],[94,19,343421],[44,22,721522],[49,81,2032198],[44,87,2156215],[80,3,5311554],[25,82,746278],[50,97,9283830],[3,45,2546055],[71,75,6527455],[40,4,1221415],[52,31,3153362],[77,38,2236446],[10,39,5566301],[8,22,2459375],[23,48,2549752],[12,19,8215990],[97,68,9354561],[43,15,8310313],[50,13,1927058],[90,83,3053924],[88,56,9090919],[95,75,8628495],[19,55,9609421],[72,95,9432224],[17,34,207337],[56,3,6440637],[73,83,2493142],[12,71,5330386],[10,33,7635076],[30,99,1627629],[65,58,6294215],[67,72,9777098],[85,31,4533946],[64,49,6649386],[65,29,9946476],[83,72,6688553],[71,92,5977834],[33,88,3336992],[55,49,3466098],[99,54,4525509],[30,24,3810453],[80,86,2265895],[51,11,1012145],[6,41,4586868],[23,28,9389947],[99,33,7545377],[29,39,8759547],[55,4,6460250],[38,81,3195116],[1,49,3796874],[27,10,5691048],[44,47,9701776]]
        source = 0
        destination = 1
        target = 162942153
        result = s.modifiedGraphEdges(n, edges, source, destination, target)
        self.assertEqual([], result)

try:
    unittest.main()
except SystemExit:
    None






