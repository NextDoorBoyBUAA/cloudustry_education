struct RetrievalRequest {
    1: i32 req_id,
    2: i32 sketch_id,
    3: string keyword,
    4: i32 count,
    5: map<i32, i32> info,
}
struct RetrievalReponse {
    1: i32 mid,
    2: double score,
}
service matrix {
    RetrievalRequest retrieval(1: RetrievalRequest request)
}