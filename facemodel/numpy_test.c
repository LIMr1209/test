#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct POINT{
    double x;
    double y;
};


int main()
{
    struct  POINT pF[20792],pP[20792], pC[20792];
    FILE* f= fopen("10.json","r");
    FILE* p= fopen("vertex_uv_coord_np.txt","r");
    int count = 0, len=1;
    // {"x":0.94606000185012817,"y":0.8853600025177002},
    // 9.479999542236328125e-03 6.620000302791595459e-02
    while (len) {
        len = fscanf(f,"{\"x\":%lf,\"y\":%lf},\n", &pF[count].x, &pF[count].y);
        fscanf(p,"%lf %lf\n", &pP[count].x, &pP[count].y);
        //printf("%d :%f, %f\n", count, pP[count].x, pP[count].y);
//        printf("%d :%f, %f\n", count, pF[count].x, pF[count].y);

        count++;
    }
    fclose(p);
    fclose(f);



    int v =0;
    for (int i =0; i < 20792; i++){
        for (int j = 0; j < 20792; j++) {
            if (memcmp(&pP[i],&pF[j],sizeof(struct POINT))==0){
                v ++;
            }

//                printf("%d, %d :%f, %f == %f, %f\n", i,j, pP[i].x, pP[i].y, pF[j].x, pF[j].y);
        }
    }
    printf("%d\n",v);

    /*
    // construct some NumCpp arrays
    auto data2 = nc::load<double>("vertex_uv_coord_np.bin");
    data2.reshape({20792,2});

    std::ofstream outputFile("output.txt");
    std::ifstream file("10.json");
    std::string jsonData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    // 解析JSON数据
    rapidjson::Document document;
    document.Parse(jsonData.c_str());

    // 检查数据是否成功解析
    if (document.HasParseError()) {
        outputFile << "Failed to parse JSON." << std::endl;
        return 1;
    }


    std::vector<std::vector<double>> temp;
    for (rapidjson::Value::ConstValueIterator it = document.Begin(); it != document.End(); ++it) {
        if (it->IsObject()) {
            const rapidjson::Value& obj = *it;
            std::vector<double> row;

//                if (obj.HasMember("x") && obj["x"].IsDouble()) {
//                    double x = obj["x"].GetDouble();
//                    outputFile << "x: " << x << std::endl;
//                }
//
//                if (obj.HasMember("y") && obj["y"].IsDouble()) {
//                    double y = obj["y"].GetDouble();
//                    outputFile << "y: " << y << std::endl;
//                }
            double x = obj["x"].GetDouble();
            double y = obj["y"].GetDouble();
            row.push_back(x);
            row.push_back(y);
            temp.push_back(row);

        }
    }
    nc::NdArray<double> data1(temp);
    for (int i = 0; i < data1.shape().rows; i++) {
        nc::NdArray<double> array = nc::tile(data2(nc::Slice(0,1), nc::Slice(0,2)), data1.shape().rows,1);
        outputFile << array << std::endl;
    }


    outputFile.close();

*/
    return 0;
}