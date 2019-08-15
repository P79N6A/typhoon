include "base.thrift"

namespace py face_predict

struct ImageInfo {
    1: string image_url,
    2: optional binary image_data,
}

struct ImagesPredictReq {
    1: list<ImageInfo> images,
    2: bool need_level = false,
    3: bool need_gender = false,
    4: bool need_race = false,
    255: optional base.Base Base,
}

struct VideoPredictReq {
    1: string video_url,
    2: optional list<ImageInfo> frames,
    3: optional map<string,string> extra,
    4: bool need_level = false,
    5: bool need_gender = false,
    6: bool need_race = false,
    255: optional base.Base Base,
}

struct FaceAttr {
    1: string tag_name,
    2: i32 tag_id,
    3: double prob,
    255: optional base.BaseResp BaseResp,
}

struct FaceAttrs {
    2: FaceAttr face_level,
    3: FaceAttr face_gender,
    4: FaceAttr face_race,
    255: optional base.BaseResp BaseResp,
}

struct FacePredictResp {
    1: list<FaceAttrs> predict_results,
    255: optional base.BaseResp BaseResp,
}


service FacePredict {
    FacePredictResp PredictImages(1: ImagesPredictReq req)
    FacePredictResp PredictVideo(1: VideoPredictReq req)
}
