import java.util.*;

class Solution {
    
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> resultList = new ArrayList<>();
        Map<String, Integer> info = new HashMap<>();

        // terms 정보를 맵에 저장
        for(String term: terms) {
            String[] x = term.split(" ");
            info.put(x[0], Integer.parseInt(x[1]));
        }

        // today를 연월일로 분해
        int[] todayDate = parseDate(today);

        // 각 개인정보별로 만료일 계산
        for(int i = 0; i < privacies.length; i++) {
            String[] tmp = privacies[i].split(" ");
            int[] privacyExpirationDate = calculate(tmp[0], tmp[1], info);

            // 오늘 날짜와 비교해서 만료된 경우 resultList에 추가
            if(isExpired(todayDate, privacyExpirationDate)) {
                resultList.add(i + 1); // 1-based index
            }
        }

        // 결과 배열 변환
        int[] answer = resultList.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }

    // 날짜를 "yyyy.mm.dd" 형식에서 분해해서 int 배열로 변환
    public int[] parseDate(String date) {
        String[] parts = date.split("\\."); // .을 이스케이프 처리
        int[] result = new int[3];
        result[0] = Integer.parseInt(parts[0]);
        result[1] = Integer.parseInt(parts[1]);
        result[2] = Integer.parseInt(parts[2]);
        return result;
    }

    // 개인정보 만료일 계산
    public int[] calculate(String startDate, String term, Map<String, Integer> info) {
        int[] start = parseDate(startDate);
        int termMonths = info.get(term);

        start[1] += termMonths; // 월을 추가

        // 월이 12를 넘으면 연도로 넘어감
        while (start[1] > 12) {
            start[0] += 1;
            start[1] -= 12;
        }

        return start;
    }

    // 만료일이 오늘 날짜보다 이전인지 확인
    public boolean isExpired(int[] today, int[] expirationDate) {
        if(today[0] > expirationDate[0]) return true;
        if(today[0] == expirationDate[0] && today[1] > expirationDate[1]) return true;
        if(today[0] == expirationDate[0] && today[1] == expirationDate[1] && today[2] >= expirationDate[2]) return true;
        return false;
    }
}
