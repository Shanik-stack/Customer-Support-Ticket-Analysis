## Human Evaluation of LLM Summary

Let us define metrics to evaluate LLM summaries.

## Evaluation Rubrik

#### Objective metrics

1. Faithfulness: Are all generated claims supported by the source?

This is measured by, Faithfulness = (Supported claims in generated summary)/(Total claims in generated summary). 

2. Salient Content Coverage:How much important reference information is preserved?

This is measured by, Salient Content Coverage = (Reference claims preserved in summary)/(Total salient claims in reference).

#### Subjective Metrics

3. Clarity and Fluency: Is the summary easy to understand and gramatically correct

4. Conciseness: How concise and information dense is the summary.

#### Normalised Score

Lets give a higher weight to the Objective metrics as they have higher importance because they are responsible in preserving information from the reference.

Let,
weight_obj = 2
weight_subj = 1

Normalised_score = 2*(Faithfullness + Salient Content Coverage) + weight_subj*(Clarity and Fluency + Conciseness) / 6

### Summaries and Evaluation

#### T1

Reference: "Customer locked out of CloudSync after resetting their password." 
LLM: "User cannot log in to CloudSync."

Evaluation:
Claims made by reference: 
1. The affected product is ClousSync
2. Customer is locked out
3. Issuee happened after resetting password

Claims made by summary:
1. User cannot log in
2. Cannot log in to CloudSync

Faithfullness: Both claims in the summary are supported by the reference
Therefore Faithfulness = 2/2 = 1.00

Salient Content Coverage: No. of claims in smmary/ No. of claims in reference = 2/3 = 0.66

Clarity and Fluency = 1, the summary is clear and gramatically correct.

Conciseness = 1, the summary is concise and information dense.

Normalised Score = (2 * (1 + 2/3) + 1 + 1) / 6 = 0.89

T2

Reference: "CloudSync sync process hangs near completion."
LLM: "Sync is stuck."

Evaluation:

Claims made by reference:

1. The issue is with synchronization
2. The affected product is CloudSync
3. The sync hangs near completion

Claims made by summary:

1. The sync is stuck.

Faithfulness: The claim made in the summary is supported by the reference.

Faithfulness = 1/1 = 1.00

Salient Content Coverage: The summary includes the synchronization problem but removes the product and the near-completion detail.

Coverage = 1/3 = 0.33

Clarity and Fluency = 1, the summary is clear and gramatically correct.

Conciseness = 1: the summary is concise and information dense. The missing details are penalized under coverage and not conciseness.

Normalised Score (T2) = (2 * (1 + 1/3) + 1 + 1) / 6 = 0.78

#### T3

Reference: "InvoicePro-generated PDFs are missing invoice line items."
LLM: "PDF export has a missing items bug in InvoicePro."

Evaluation:

Claims made by reference:

1. The affected product is the InvoicePro
2. The issue is with the  generated PDF
3. Invoice line items are missing from the PDFs

Claims made by summary:

1. The issue is with the PDF export
2. Items are missing from the exported PDF
3. The affected product is InvoicePro

Faithfulness: All three claims are consistent with the reference. 
Faithfulness = 3/3 = 1.00

Salient Content Coverage: The product and PDF-export context are preserved. “Missing items” doesnt include the more specific detail “missing invoice line items,” so it receives 0.5 credit.

Salient Content Coverage = (1 + 1 + 0.5) / 3 = 2.5/3 = 0.83

Clarity and Fluency = 1, The issue is clear and the sentence is grammatically acceptable.

Conciseness = 1, the summary is concise and information dense

Normalised Score (T3) = (2 * (1 + 2.5/3) + 1 + 1) / 6 = 0.94

| Ticket | Faithfulness | Salient Content Coverage | Clarity and Fluency | Conciseness | Normalised Score |
| --- | --- | --- | --- | --- | --- |
| T1  | 1.00 | 0.67 | 1.00 | 1.00 | 0.89 |
| T2  | 1.00 | 0.33 | 1.00 | 1.00 | 0.78 |
| T3  | 1.00 | 0.83 | 1.00 | 1.00 | 0.94 |

These are manually assigned scores and can vary between evaluators, this is especially true for the subjective metrics. Thus having an explicit breakdown makes the scoring auditable. The checks are done using the rubric defined in the beginning.