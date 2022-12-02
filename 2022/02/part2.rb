round_scores = {
  "X" => 0,
  "Y" => 3,
  "Z" => 6,
}

throw_scores = {
  "A" => 1,
  "B" => 2,
  "C" => 3,
}

throws = ["A", "B", "C"]

rounds = File.read("strategy.txt").strip().split("\n")

total_score = 0

for round in rounds
  opponent_throw = round.split[0]
  opponent_throw_index = throws.find_index(opponent_throw)
  round_outcome = round.split[1]
  total_score += round_scores[round_outcome]
  if round_outcome == "X"
    total_score += throw_scores[throws[opponent_throw_index - 1]]
    next
  elsif round_outcome == "Z"
    total_score += throw_scores[throws[opponent_throw_index - 2]]
    next
  else
    total_score += throw_scores[opponent_throw]
  end
end

puts "this outcome will yield a total score of #{total_score}"
