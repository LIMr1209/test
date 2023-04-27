#/bin/bash
echo  $1"\n"
curl http://10.25.10.132:8006/admin/face_image_auto/save -F "file=@$1;"  -F name=$2 -F cue_word=测试 -H 'Cookie: session=9a46fa78-04de-48c6-bb8d-2678002f9aa2.YSO8GGhnxraWeFMgjafxB3WJNuE'
